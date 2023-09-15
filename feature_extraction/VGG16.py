
# Importing the required modules
import numpy as np
import tensorflow as tf
from PIL import Image
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Model
from keras.applications.inception_v3 import InceptionV3
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
# from tensorflow.keras.models import Model


class FeatureExtractionUsingVGG16:

    def __init__(self, path):
        self.path = path

        # Checking for the GPU for faster computation
        print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
        print(tf.test.is_built_with_cuda())

        # Use VGG-16 as the architecture and ImageNet for the weight
        base_model = VGG16(weights = 'imagenet')

        # Customize the model to return features from fully-connected layer
        self.model = Model(inputs = base_model.input, outputs = base_model.get_layer('fc1').output)

    def extract(self, filename):

        # Reading the image
        img = Image.open(self.path + filename)
        # Resize the image
        img = img.resize((224, 224))
        # Convert the image color space to RGB
        img = img.convert('RGB')

        # Reformat the image
        # x = np.array(img)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis = 0)
        x = preprocess_input(x)

        # Extract Features
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)

    def saveFeatures(self, features):
        # Save the Numpy array (.npy) on designated path
        np.save(self.path + 'VGG16_features1_.npy', features)
        print("Features successfully extracted, and stored at " + self.path + 'VGG16_features_.npy' + "...\n")

    def __call__(self, *args, **kwargs):
        feat = self.extract(kwargs["filename"])
        self.saveFeatures(feat)

    def __del__(self):
        pass