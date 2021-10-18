import glob
import os.path
files = glob.glob(".//*//*.jpg")
for x in files:
  if not os.path.isdir(x):
    filename = os.path.splitext(x)
    try:
      os.rename(x,filename[0] + '.png')
    except:
      pass