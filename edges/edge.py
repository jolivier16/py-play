#python image lib
from PIL import Image, ImageFilter

before = Image.open("cyber japan.jpeg")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("edges.jpg")