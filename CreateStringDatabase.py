# Importing all our own modules for integration
from ocr.ocr import OCR

images = ['1.png', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
path = ".\\feature_database\\"

for img in images:
    ocr = OCR(img, path)
    ocr()
    ocr.__del__()