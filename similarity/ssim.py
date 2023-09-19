from skimage.metrics import structural_similarity
import cv2
import numpy as np

class StructuralSimilarityIndex:

    def __init__(self):
        self.img1 = None
        self.img2 = None

    def score(self, img1, img2):
        self.img1 = img1
        self.img2 = img2

        score, diff = structural_similarity(self.img1.reshape(1, -1), self.img2.reshape(1, -1), data_range = 1, full = True, gaussian_weights = False, use_sample_covariance = False)
        return score * 100

    def __call__(self, *args, **kwargs):
        pass

    def __del__(self):
        pass