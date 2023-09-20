print(" ................................. START .................................. ")

# Importing all our own modules for integration
print("Importing all our own local & pip modules for integration...")
import os
import shutil
from pdf2image import convert_from_path
from ocr.ocr import OCR
from ner.lvl1 import CustomNER
from ner.lvl2 import BasicNER
from ner.lvl3 import MedicalNER
from ner.regex import Regex
from optimization import NER_Checking
from FraudDetection import FraudDetection
from mongoDB.DatabaseConnection import MongoDB


if __name__ == "__main__":

    # Defining the path of Feature Database
    path = ".\\feature_database\\"

    # Accessing MongoDB & extracting data from it
    source = "..\\server\\fileUpload\\"
    destination = ".\\fromServer\\"

    mongo = MongoDB()
    data = mongo.getData()
    filenameEncy = data.get('filePath')[11:]
    img = data.get('fileName')
    mongo.__del__()

    dirFiles = os.listdir(source)
    shutil.copy(source + filenameEncy, destination + img)

    print("Uploaded Encrypted Filename :", filenameEncy, '...')
    print("File uploaded in server is stored in ", destination + img, "...")

    # Converting pdf to jpg
    pages = convert_from_path(destination + img)
    pages[0].save(path + img[0:-4] + '.jpg', 'JPEG')
    print("The input file is converted into .jpg and stored at ", path + img[0:-4] + '.jpg', "...")
    img = img[0:-4] + '.jpg'

    # Extracting Text from the given image
    ocr = OCR(img, path)
    text = ocr()
    # text = text.replace("\n", " ")
    ocr.__del__()

    # Extracting important entities from extracted string
    medicine, medical_cond, pathogens, names2, doctor, date, phone, address, postal_code = \
        [], [], [], [], [], [], [], [], []

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

    # Filtering the NERs output
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
    print("\nPrinting Filtered Extracted Entities...")
    print("NAME: ", rt['name'])
    print("DOCTOR: ", rt['doctor'])
    print("PHONE: ", rt['phone'])
    print("DATE: ", rt['date'])
    print("ADDRESS: ", rt['address'])
    print("RUPEES: ", rt['amount'])
    print("INVOICE: ", rt['invoice'])
    print("GST NUMBER: ", rt['gst'])
    print("ORGANIZATION: ", rt['org'])
    print("MEDICINES: ", rt['medicines'])
    print("MEDICAL CONDITIONS: ", rt['MedCond'])
    print("PATHOGENS: ", rt['pathogens'])
    print("\n")

    # Fraud Detection, which return flag colours as per the risk value
    frd = FraudDetection(text, img, path)
    scr, col = frd()
    print("Similarity Score : ", scr)
    print("Flag Colour : ", col)
    frd.__del__()

    # Accessing MongoDB & uploading data into it
    mongo = MongoDB()
    id = mongo.addData(filename = img[0:-4] + ".pdf", name = rt['name'], doctor = rt['doctor'],
                       phone = rt['phone'], date = rt['date'], address = rt['address'],
                       rupees = rt['amount'], invoice = rt['invoice'], gst = rt['gst'],
                       org = rt['org'], med = rt['medicines'], medCond = rt['MedCond'],
                       pathogens = rt['pathogens'], fraudColor = col)
    print("Extracted entities of file ", filenameEncy, " is again stored in MongoDB...")
    mongo.__del__()




    print(" ................................. END .................................. ")