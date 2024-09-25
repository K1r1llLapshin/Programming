from pathlib import Path
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-ftype")

files = list(Path(".").glob("*."+ parser.parse_args().ftype))

for file in files:
    with Image.open(file) as img:
        img = img.resize((50,50))
        img.show()
