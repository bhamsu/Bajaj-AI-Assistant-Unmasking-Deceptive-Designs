# Importing all our own modules for integration
import os

if __name__ == "__main__":

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

    print(os.listdir("..\\server\\fileUpload"))