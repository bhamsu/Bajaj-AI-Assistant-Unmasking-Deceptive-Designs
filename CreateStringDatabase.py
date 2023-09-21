# Importing all our own modules for integration
from ocr.ocr import OCR
import os

path = ".\\feature_database\\"
images = [f for f in os.listdir(path) if f.endswith('.jpg')]

for img in images:
    ocr = OCR(img, path)
    ocr()
    ocr.__del__()