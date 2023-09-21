# Importing all our own modules for integration
from feature_extraction.FasterRCNN import FeatureExtractionUsingFasterRCNN
from feature_extraction.VGG16 import FeatureExtractionUsingVGG16
import os

path = ".\\feature_database\\"
images = [f for f in os.listdir(path) if f.endswith('.jpg')]

"""for img in images:
    fe = FeatureExtractionUsingFasterRCNN(path)
    fe(filename = img)
    fe.__del__()"""

for img in images:
    fe = FeatureExtractionUsingVGG16(path)
    fe(filename = img)
    fe.__del__()