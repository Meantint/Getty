import glob
import os
from PIL import Image
files = glob.glob('.//*//*.png')

for file in files:
    title, ext = os.path.splitext(file)
    img = img = Image.open(file)
    img_resize = img.resize((256, 256))
    img_resize.save(title+ext)