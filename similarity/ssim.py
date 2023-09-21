from skimage.metrics import structural_similarity
import cv2
import numpy as np

class StructuralSimilarityIndex:

    def __init__(self):
        self.img1 = None
        self.img2 = None

    def score(self, img1, img2, fe):
        self.img1 = img1
        self.img2 = img2

        if fe == 'VGG16':
            # score, diff = structural_similarity(self.img1.reshape(1, -1), self.img2.reshape(1, -1), data_range = 1, full = True, gaussian_weights = False, use_sample_covariance = False)
            score = structural_similarity(self.img1.squeeze(), self.img2.squeeze(), multichannel = True, data_range = 1.0)
            return score * 100
        elif fe == 'FasterRCNN':
            score = structural_similarity(np.asarray(self.img1), np.asarray(self.img2))
            return score * 100
        else:
            print("Error occurred at ssim script.")
            return -1

    def __call__(self, *args, **kwargs):
        pass

    def __del__(self):
        pass