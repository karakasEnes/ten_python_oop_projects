import numpy
import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

        self.data = numpy.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def create(self, image_path):
        img = Image.fromarray(self.data, mode="RGB")
        img.save(image_path)
