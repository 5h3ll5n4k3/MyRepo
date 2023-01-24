from PIL import Image, ImageDraw, ImageFont
import random

class Penguin:
    def __init__(self, file_path):
        self.image = Image.open(file_path)
        self.accessory = None

    def set_accessory(self, accessory):
        draw = ImageDraw.Draw(self.image)
        if accessory == "hat":
            # code to draw a hat on the image
            pass
        elif accessory == "scarf":
            # code to draw a scarf on the image
            pass
        elif accessory == "sunglasses":
            # code to draw sunglasses on the image
            pass
        elif accessory == "bow tie":
            # code to draw a bow tie on the image
            pass
        self.accessory = accessory

    def save(self, file_path):
        self.image.save(file_path)

penguins = []
accessories = ["hat", "scarf", "sunglasses", "bow tie"]

for i in range(5):
    penguin = Penguin("penguin.jpg")
    penguin.set_accessory(random.choice(accessories))
    penguins.append(penguin)

for i, penguin in enumerate(penguins):
    penguin.save(f"penguin_{i}.jpg")
