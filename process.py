import glob
import shutil
import os
from PIL import Image


class Digitizer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.img = Image.open(filepath)

    def make_upside_down(self):
        print("Make upside down")
        self.img = self.img.rotate(180)

    def save(self, output_filepath):
        self.img.save(output_filepath)


inputs = glob.glob("inputs/*.jpg")

os.makedirs("outputs", exist_ok=True)

for filepath in inputs:
    output = filepath.replace("inputs", "outputs")
    image = Digitizer(filepath)
    image.make_upside_down()
    image.save(output)

