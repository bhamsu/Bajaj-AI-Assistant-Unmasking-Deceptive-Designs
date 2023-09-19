# Importing all our own modules for integration
from feature_extraction.FasterRCNN import FeatureExtractionUsingFasterRCNN
from feature_extraction.VGG16 import FeatureExtractionUsingVGG16

images = ['1.png', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
path = ".\\feature_database\\"

for img in images:
    fe = FeatureExtractionUsingFasterRCNN(path)
    fe(filename = img)
    fe.__del__()

for img in images:
    fe = FeatureExtractionUsingVGG16(path)
    fe(filename = img)
    fe.__del__()