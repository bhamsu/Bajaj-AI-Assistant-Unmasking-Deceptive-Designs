# Importing all our own modules for integration
from ocr.ocr import OCR
from ner.lvl1 import CustomNER
from ner.lvl2 import BasicNER
from ner.lvl3 import MedicalNER
from ner.regex import Regex
from optimization import NER_Checking
from FraudDetection import FraudDetection

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




    img = "6.jpg"
    path = ".\\feature_database\\"

    # Extracting Text from image/PDFs
    ocr = OCR(img, path)
    text = ocr()
    text = text.replace("\n", " ")
    ocr.__del__()
    # print(text.replace("\n", " "))
    """
    # Extracting important entities from extracted string
    medicine, medical_cond, pathogens, names2, doctor, date, phone, address, postal_code = \
        [], [], [], [], [], [], [], [] ,[]

    ner_basic = BasicNER()
    names, organizations = ner_basic.test(text)

    ner_medical = MedicalNER(".\\model-data\\")
    medical_ner_rslt = ner_medical.test(text)

    for ent in medical_ner_rslt.ents:
        if ent.label_ == "MEDICINE":
            medicine.append(ent.text)
        if ent.label_ == "MEDICALCONDITION":
            medical_cond.append(ent.text)
        if ent.label_ == "PATHOGEN":
            pathogens.append(ent.text)

    ner_custom = CustomNER(".\\model-data\\")
    custom_ner_rslt = ner_custom.test(text)

    for ent in custom_ner_rslt.ents:
        if ent.label_ == "PERSON":
            names2.append(ent.text)
        if ent.label_ == "DOCTOR":
            doctor.append(ent.text)
        if ent.label_ == "DATE":
            date.append(ent.text)
        if ent.label_ == "PHONE":
            phone.append(ent.text)
        if ent.label_ == "ADDRESS":
            address.append(ent.text)
        if ent.label_ == "POSTAL_CODE":
            postal_code.append(ent.text)

    reg = Regex(text)
    """
    """print("NAMES: ", names)
    print("NAMES2: ", names2)
    print("DOCTORS: ", doctor)
    print("DOCTORS2: ", reg.findDr())
    print("MEDICINES: ", medicine)
    print("MEDICAL CONDITIONS: ", medical_cond)
    print("PATHOGENS: ", pathogens)
    print("ORGANIZATIONS: ", organizations)
    print("GST NUMBER: ", reg.findGST())
    print("INVOICE: ", reg.findInvoice())
    print("RUPEES: ", reg.findRupees())
    print("DATE: ", date)
    print("PHONE1: ", phone)
    print("PHONE2: ", reg.findPhone())
    print("ADDRESS: ", address)
    print("POSTAL CODE: ", postal_code, "\n\n\n")"""

    """# Filtering the NERs output
    check = NER_Checking()
    rt = check(names = names, names2 = names2, doctors = reg.findDr(), phones = reg.findPhone(),
               date = date, address = address, amounts = reg.findRupees(), invoices = reg.findInvoice(),
               gst = reg.findGST(), org = organizations, medicines = medicine, MedCond = medical_cond,
               pathogens = pathogens)

    ner_basic.__del__()
    ner_medical.__del__()
    ner_custom.__del__()
    reg.__del__()
    check.__del__()


    # Printing the extracted & filtered entities
    print("NAMES: ", rt['name'])
    print("DOCTORS: ", rt['doctor'])
    print("PHONE: ", rt['phone'])
    print("DATE: ", rt['date'])
    print("ADDRESS: ", rt['address'])
    print("RUPEES: ", rt['amount'])
    print("INVOICE: ", rt['invoice'])
    print("GST NUMBER: ", rt['gst'])
    print("ORGANIZATIONS: ", rt['org'])
    print("MEDICINES: ", rt['medicines'])
    print("MEDICAL CONDITIONS: ", rt['MedCond'])
    print("PATHOGENS: ", rt['pathogens'])"""

    """# Extracting features of input image
    fe = FeatureExtractionUsingFasterRCNN(path)
    feature = fe(filename = img)

    # Matching Algorithm
    match = Matching(path)
    str_Score, img_Score = match(imgFt = feature, strFt = text)
    print(str_Score)"""

    frd = FraudDetection(text, img, path)
    print(frd())


