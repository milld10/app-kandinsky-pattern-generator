import os

from PIL import Image
from kp import KandinskyUniverse, RandomKandinskyFigure, SimpleObjectAndShape, ShapeOnShapes, KandinskyCaptions, \
    PatternGenerator

u = KandinskyUniverse.SimpleUniverse()
cg = KandinskyCaptions.CaptionGenerator(u)


def generateImagesAndCaptions(basedir, kfgen, n=50):
    os.makedirs(basedir, exist_ok=True)
    capt_color_shape_size_file = open(basedir + "/color_shape_size.cap", "w")
    capt_numbers = open(basedir + "/numbers.cap", "w")
    for (i, kf) in enumerate(kfgen.true_kf(n)):
        image = KandinskyUniverse.kandinskyFigureAsImage(kf)
        image.save(basedir + "/%06d" % i + ".png")
        capt_color_shape_size_file.write(str(i) + '\t' + cg.colorShapesSize(kf, 'one ') + '\n')
        capt_numbers.write(str(i) + '\t' + cg.numbers(kf) + '\n')
    capt_color_shape_size_file.close()
    capt_numbers.close()


# saves images into directory
# n will be ignored if n is set differently at method call; default is 50
def generateClasses(basedir, kfgen, n=50, contrafactuals=False):
    os.makedirs(basedir + "/true", exist_ok=True)
    os.makedirs(basedir + "/false", exist_ok=True)
    for (i, kf) in enumerate(kfgen.true_kf(n)):
        image = KandinskyUniverse.kandinskyFigureAsImage(kf)
        image.save(basedir + "/true/%06d" % i + ".png")
    for (i, kf) in enumerate(kfgen.false_kf(n)):
        image = KandinskyUniverse.kandinskyFigureAsImage(kf)
        image.save(basedir + "/false/%06d" % i + ".png")
    if (contrafactuals):
        os.makedirs(basedir + "/contrafactuals", exist_ok=True)
        for (i, kf) in enumerate(kfgen.almost_true_kf(n)):
            image = KandinskyUniverse.kandinskyFigureAsImage(kf)
            image.save(basedir + "/contrafactuals/%06d" % i + ".png")


if (__name__ == '__main__'):
    print('Welcome to the Kandinsky Figure Generator')

    numberOfImages = 20

    # my generators:
    onesquare = PatternGenerator.oneSquare(u, 4, 4)
    generateClasses("../test/oneSquare", onesquare, numberOfImages)

    onlyRed = PatternGenerator.onlyRed(u, 4, 4)
    generateClasses("../test/onlyRed", onlyRed, numberOfImages)

    onlyCircles = PatternGenerator.onlyCircles(u, 4, 4)
    generateClasses("../test/onlyCircles", onlyCircles, numberOfImages)

    # descendingShapes = PatternGenerator.descendingShapes(u, 4, 4)
    # generateClasses("../test/descendingShapes", descendingShapes, numberOfImages)

    #
    randomkf = RandomKandinskyFigure.Random(u, 4, 6)
    generateImagesAndCaptions("../test/randomkf", randomkf, numberOfImages)

    redobjects = SimpleObjectAndShape.ContainsRedObjects(u, 4, 4)
    generateClasses("../test/onered", redobjects, numberOfImages)

    triangleobjects = SimpleObjectAndShape.ContainsTriangles(u, 4, 4)
    generateClasses("../test/onetriangle", triangleobjects, numberOfImages)

    shapeOnshapeObjects = ShapeOnShapes.ShapeOnShape(u, 20, 40)
    generateClasses("../test/shapeonshapes", shapeOnshapeObjects, numberOfImages, contrafactuals=True)
