import math

import numpy as np
from PIL import Image, ImageDraw


class kandinskyShape:
    def __init__(self):
        self.shape = "circle"
        self.color = "red"
        self.x = 0.5
        self.y = 0.5
        self.size = 0.5

    def __str__(self):
        return self.color + " " + self.shape + " (" + \
               str(self.size) + "," + str(self.x) + "," + str(self.y) + ")"


class SimpleUniverse:
    kandinsky_colors = ['red', 'yellow', 'blue']
    kandinsky_shapes = ['square', 'circle', 'triangle']


class ExtendedUniverse:
    # still have to add drawing functions below
    kandinsky_colors = ['red', 'yellow', 'blue', "green", "orange"]
    kandinsky_shapes = ['square', 'circle', 'triangle', "star"]


# Math Functions of simple universe
def square(d, cx, cy, s, f):
    s = 0.7 * s
    d.rectangle(((cx - s / 2, cy - s / 2), (cx + s / 2, cy + s / 2)), fill=f)


def circle(d, cx, cy, s, f):
    # correct the size to  the same area as an square
    s = 0.7 * s * 4 / math.pi
    d.ellipse(((cx - s / 2, cy - s / 2), (cx + s / 2, cy + s / 2)), fill=f)


def triangle(d, cx, cy, s, f):
    r = math.radians(30)
    # correct the size to  the same area as an square
    s = 0.7 * s * 3 * math.sqrt(3) / 4
    dx = s * math.cos(r) / 2
    dy = s * math.sin(r) / 2
    d.polygon([(cx, cy - s / 2), (cx + dx, cy + dy), (cx - dx, cy + dy)], fill=f)


# Gets an array of shapes and creates image
def kandinskyFigureAsImage(shapes, width=200, subsampling=2):
    image = Image.new("RGBA", (subsampling * width, subsampling * width), (220, 220, 220, 255))
    d = ImageDraw.Draw(image)
    w = subsampling * width
    for s in shapes:
        globals()[s.shape](d, w * s.x, w * s.y, w * s.size, s.color)
    if subsampling > 1:
        image.thumbnail((width, width), Image.ANTIALIAS)

    return image


def overlaps(shapes, width=1024):
    image = Image.new("L", (width, width), 0)
    sumarray = np.array(image)
    d = ImageDraw.Draw(image)
    w = width
    for s in shapes:
        image = Image.new("L", (width, width), 0)
        d = ImageDraw.Draw(image)
        globals()[s.shape](d, w * s.x, w * s.y, w * s.size, 10)
        sumarray = sumarray + np.array(image)
    sumimage = Image.fromarray(sumarray)
    return sumimage.getextrema()[1] > 10
