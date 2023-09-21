# Importing all our own modules for integration
from MatchingAlgorithm import Matching
from feature_extraction.FasterRCNN import FeatureExtractionUsingFasterRCNN
from feature_extraction.VGG16 import FeatureExtractionUsingVGG16

class FraudDetection:

    def __init__(self, text, img, path):
        self.text = text
        self.img = img
        self.path = path

        # Setting the threshold values for detecting potential or suspicious frauds
        self.amber_threshold = 45   # Suspicion Threshold
        self.red_threshold = 70     # Potential Fraud
        self.str_threshold = 36
        print("Fraud Detection started...")

    def detection(self):

        # Extracting features of input image
        fe = FeatureExtractionUsingVGG16(self.path)
        feature = fe(filename = self.img)

        # Matching Algorithm
        match = Matching(self.path)
        str_Score, img_Score = match(imgFt = feature, strFt = self.text)

        return str_Score, img_Score

    def __call__(self, *args, **kwargs):

        str_score, img_Score = self.detection()
        score = (str_score + img_Score) / 2 # divide by 2
        color = "error"
        print(str_score, img_Score)

        """if str_score < self.amber_threshold:
            if img_Score < self.red_threshold:
                color = "green"
            else:
                color = "amber"
        elif self.amber_threshold < str_score < self.red_threshold:
            if img_Score > self.red_threshold:
                return "red"
            else:
                color = "amber"
        elif str_score > self.red_threshold:
            if self.amber_threshold < img_Score:
                color = "red"
            else:
                color = "amber"
        else:
            color = "red"
        """

        if score < self.amber_threshold:
            color = "green"
        elif self.red_threshold > score > self.amber_threshold:
            if str_score < self.str_threshold:
                color = "green"
            else:
                color = "amber"
        else:
            color = "red"

        print("Fraud Detection ended...")
        return color

    def __del__(self):
        pass