import glob
import shutil
import os
from PIL import Image, ImageOps, ImageEnhance


class Digitizer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.img = Image.open(filepath)

    def make_upside_down(self):
        print("Make upside down")
        self.img = self.img.rotate(180)

    def make_thumbnail_size(self, size=(128, 128)):
        self.img.thumbnail(size)

    def make_square(self, size=200):
        self.img = self.img.resize((size, size))

    def make_grayscale(self):
        self.img = ImageOps.grayscale(self.img)

    def adjust_contrast(self, amount=1.5):
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(amount)

    def save(self, output_filepath):
        self.img.save(output_filepath)


inputs = glob.glob("inputs/*.jpg")

os.makedirs("outputs", exist_ok=True)

for filepath in inputs:
    output = filepath.replace("inputs", "outputs")
    image = Digitizer(filepath)
    image.make_thumbnail_size((200, 200))
    image.make_grayscale()
    image.make_upside_down()
    image.save(output)

