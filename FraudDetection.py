# Importing all our own modules for integration
from MatchingAlgorithm import Matching
from feature_extraction.FasterRCNN import FeatureExtractionUsingFasterRCNN

class FraudDetection:

    def __init__(self, text, img, path):
        self.text = text
        self.img = img
        self.path = path

        # Setting the threshold values for detecting potential or suspicious frauds
        self.amber_threshold = 70   # Suspicion Threshold
        self.red_threshold = 83     # Potential Fraud
        print("Fraud Detection started...")

    def detection(self):

        # Extracting features of input image
        fe = FeatureExtractionUsingFasterRCNN(self.path)
        feature = fe(filename = self.img)

        # Matching Algorithm
        match = Matching(self.path)
        str_Score, img_Score = match(imgFt = feature, strFt = self.text)

        # print(str_Score)
        return str_Score, img_Score

    def __call__(self, *args, **kwargs):

        str_score, img_Score = self.detection()
        score = str_score + img_Score  # divide by 2

        if str_score < self.amber_threshold:
            return score, "white"       # Safe
        elif self.amber_threshold < str_score < self.red_threshold:
            return score, "amber"
        elif str_score > self.red_threshold:
            return score, "red"
        else:
            print("EXCEPTION: NO CONDITION SATISFIED.")

        print("Fraud Detection ended...")

    def __del__(self):
        pass