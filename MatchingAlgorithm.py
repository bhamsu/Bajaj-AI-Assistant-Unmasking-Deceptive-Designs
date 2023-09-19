# Importing all the required modules
import os
import numpy as np
from similarity.cosine_match import CosineSimilarity
from similarity.jaccard_sim import JaccardSimilarity
from similarity.ssim import StructuralSimilarityIndex


class Matching:

    def __init__(self, path):
        self.path = path

    def readDir(self):
        txt_files = [f for f in os.listdir(self.path) if f.endswith('.txt')]
        npy_files = [f for f in os.listdir(self.path) if f.endswith('.npy')]

        return txt_files, npy_files

    def StringMatch(self, strFt, txt_files):

        max_Score = 0
        for file in txt_files:
            with open(self.path + file, "r") as fp:
                score = (CosineSimilarity().score(strFt, fp.read(), img = False) + JaccardSimilarity().score(strFt, fp.read())) / 2
                if score > max_Score:
                    max_Score = score
        return max_Score

    def FeatureMatching(self, imgFt, npy_files):

        max_Score = 0
        for file in npy_files:
            fp = np.load(self.path + file)
            score = (CosineSimilarity().score(imgFt, fp, img = True) + StructuralSimilarityIndex().score(imgFt, fp)) / 2
            if score > max_Score:
                max_Score = score
        return max_Score

    def __call__(self, *args, **kwargs):

        txt_files, npy_files = self.readDir()

        str_Score = self.StringMatch(kwargs['strFt'], txt_files)
        img_score = self.FeatureMatching(kwargs['imgFt'], npy_files)

        return str_Score, img_score

    def __del__(self):
        pass
