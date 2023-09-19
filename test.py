# Importing all our own modules for integration
from feature_extraction.FasterRCNN import FeatureExtractionUsingFasterRCNN
from feature_extraction.VGG16 import FeatureExtractionUsingVGG16
import numpy as np
from similarity.cosine_match import CosineSimilarity
from similarity.jaccard_sim import JaccardSimilarity
from similarity.lavenshtein import LevenshteinDistance
from sklearn.metrics.pairwise import cosine_similarity

if __name__ == "__main__":
    """fe_rcnn = FeatureExtractionUsingFasterRCNN(".\\sample-data\\")
    fe_rcnn(filename = "1.png")

    fe_vgg = FeatureExtractionUsingVGG16(".\\sample-data\\")
    fe_vgg(filename = "1.png")

    # Example usage
    str1 = "In the bustling city of Mumbai, Mr. Subham Das, a patient at Apollo Hospitals, " \
           "visited Dr. Priya Patel, a renowned cardiologist, on September 10, 2023, for a " \
           "consultation regarding his hypertension condition. Dr. Patel prescribed him Acetaminophen, " \
           "Gabapentin, Etoposide, to manage his Fever from Salmonella and Hepatitis A. The invoice for the consultation, " \
           "issued by Apollo Hospitals (GSTIN: 06BZAHM6385P6Z2) is total Rs 15,000, was #INV-2023-12375, and Mr. Sharma's " \
           "contact number is +91 9876588210. His address, 123 Park Street, South Mumbai, is conveniently " \
           "located for medical appointments."
    str2 = "In the bustling city of Kolkata, Mr. Rajesh Sharma, a patient at Apollo Hospitals, " \
           "visited Dr. Priya Patel, a renowned gynacologist, on September 10, 2021, for a " \
           "consultation regarding his hypertension condition. Dr. Patel prescribed him Acetaminophen, " \
           "Gabapentin, Etoposide, to manage his Constipation from Salmonella and Hepatitis B. The invoice for the consultation, " \
           "issued by Apollo Hospitals (GSTIN: 06BZAHM6385P6Z7) is total Rs 10,499, was #INV-2023-12345, and Mr. Karma's " \
           "contact number is +91 9876543210. His address, 24B/3 Park Street, Kolkata, is conveniently " \
           "located for medical appointment."


    print("Percentage Cosine Similarity    : ", CosineSimilarity().score(str1, str2))
    print("Percentage Jaccard Similarity   : ", JaccardSimilarity().score(str1, str2))
    print("Percentage Levenshtein Distance : ", LevenshteinDistance().__call__(string1 = str1, string2 = str2))"""

    fe_vgg = FeatureExtractionUsingVGG16(".\\sample-data\\")
    fe_vgg(filename = "2.jpg")
    features_fcnn = np.load(".\\sample-data\\VGG16_features1_.npy")
    features_vgg = np.load(".\\sample-data\\VGG16_features_.npy")

    sim = CosineSimilarity().score(features_fcnn, features_vgg, img = True)
    print(sim)