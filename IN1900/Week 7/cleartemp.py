
import glob,os
for filename in glob.glob("temp*.png"):
    os.remove(filename)
