import PIL
import random
import numpy as np

from .KandinskyTruth import KandinskyTruthInterface
from .RandomKandinskyFigure import Random


# exactly one type of shape
class oneSquare(KandinskyTruthInterface):

    def isfuzzy(self):
        return False

    def humanDescription(self):
        return "image with exactly one square"

    def true_kf(self, n):
        kfs = []
        i = 0
        randomKFgenerator = Random(self.u, self.min, self.max)
        while i < n:
            kf = randomKFgenerator.true_kf(1)[0]
            squareCnt = 0
            for s in kf:
                if s.shape == "square":
                    squareCnt = squareCnt + 1
                if squareCnt > 0:
                    continue
            if squareCnt == 1:
                kfs.append(kf)
                i = i + 1
        return kfs

    def false_kf(self, n):
        randomKFgenerator = Random(self.u, self.min, self.max)
        kfs = randomKFgenerator.true_kf(n)
        for kf in kfs:
            for s in kf:
                if s.shape == "square":
                    s.shape = "circle"
        return kfs


# all shapes in only one color
class onlyRed(KandinskyTruthInterface):

    def isfuzzy(self):
        return False

    def humanDescription(self):
        return "image with only red shapes"

    def true_kf(self, n):
        kfs = []
        i = 0
        randomKFgenerator = Random(self.u, self.min, self.max)
        while i < n:
            kf = randomKFgenerator.true_kf(1)[0]
            for s in kf:
                s.color = "red"
            kfs.append(kf)
            i = i + 1
        return kfs

    def false_kf(self, n):
        randomKFgenerator = Random(self.u, self.min, self.max)
        kfs = randomKFgenerator.true_kf(n)
        for kf in kfs:
            for s in kf:
                if s.color == "red":
                    s.color = random.choice(["blue", "yellow"])
        return kfs


# exactly one type of shape in all colors
class onlyCircles(KandinskyTruthInterface):

    def isfuzzy(self):
        return False

    def humanDescription(self):
        return "image with only circles of all colors"

    def true_kf(self, n):
        kfs = []
        i = 0
        randomKFgenerator = Random(self.u, self.min, self.max)
        while i < n:
            kf = randomKFgenerator.true_kf(1)[0]
            for s in kf:
                s.shape = "circle"
            kfs.append(kf)
            i = i + 1
        return kfs

    def false_kf(self, n):
        randomKFgenerator = Random(self.u, self.min, self.max)
        kfs = randomKFgenerator.true_kf(n)
        for kf in kfs:
            for s in kf:
                if s.shape == "circle":
                    s.shape = random.choice(["square", "triangle"])
        return kfs

# sorts shapes by size from top to bottom in the image
# not yet working properly
# class descendingShapes(KandinskyTruthInterface):
#
#     def isfuzzy(self):
#         return False
#
#     def humanDescription(self):
#         return "sorts shapes; small are on top, big on the bottom of the image"
#
#     def true_kf(self, n):
#         kfs = []
#         kf_sorted = []
#         i = 0
#         randomKFgenerator = Random(self.u, self.min, self.max)
#         while i < n:
#             kf = randomKFgenerator.true_kf(1)[0]
#             #sorts kf by size of the shapes
#             kf.sort(key=lambda x: x.size)
#             for s in kf:
#                 # now assign new random y position, so that smallest shapes are on the top
#                 if (s.size > 0.1) and (s.size < 0.33):
#                     s.y = random.uniform(0.1, 0.33)
#                 if (s.size > 0.33) and (s.size < 0.66):
#                     s.y = random.uniform(0.33, 0.66)
#                 if (s.size > 0.66) and (s.size < 1):
#                     s.y = random.uniform(0.66, 1)
#
#             kfs.append(kf)
#             i = i + 1
#         return kfs
