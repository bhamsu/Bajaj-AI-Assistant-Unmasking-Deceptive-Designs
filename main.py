# Importing all our own modules for integration
from ocr.ocr import OCR
from ner.lvl1 import CustomNER
from ner.lvl2 import BasicNER
from ner.lvl3 import MedicalNER
from ner.regex import Regex
from optimization import NER_Checking
from FraudDetection import FraudDetection


if __name__ == "__main__":

    img = "6.jpg"
    path = ".\\feature_database\\"

    # Extracting Text from image/PDFs
    ocr = OCR(img, path)
    text = ocr()
    text = text.replace("\n", " ")
    ocr.__del__()
    # print(text.replace("\n", " "))

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
    print("PATHOGENS: ", rt['pathogens'])

    # Fraud Detection, which return flag colours as per the risk value
    frd = FraudDetection(text, img, path)
    print(frd())
    frd.__del__()