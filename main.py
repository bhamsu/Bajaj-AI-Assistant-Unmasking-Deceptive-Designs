# Importing all our own modules for integration
from ocr.ocr import OCR
from ner.lvl1 import CustomNER
from ner.lvl2 import BasicNER
from ner.lvl3 import MedicalNER
from ner.regex import Regex
from optimization import NER_Checking


if __name__ == "__main__":
    para = "In the bustling city of Mumbai, Mr. Rajesh Sharma, a patient at Apollo Hospitals, " \
       "visited Dr. Priya Patel, a renowned cardiologist, on September 10, 2023, for a " \
       "consultation regarding his hypertension condition. Dr. Patel prescribed him Acetaminophen, " \
       "Gabapentin, Etoposide, to manage his Fever from Salmonella and Hepatitis A. The invoice for the " \
       "consultation, issued by Apollo Hospitals (GSTIN: 06BZAHM6385P6Z2) is total Rs 10,499, was " \
       "#INV-2023-12345, and Mr. Sharma's contact number is +91 9876543210. His address, 123 Park Street, " \
       "South Mumbai, is conveniently located for medical appointments."



    """ocr = OCR("3.jpg", ".\\sample-data\\")
    print(ocr())"""

    ner_basic = BasicNER()
    names, organizations = ner_basic.test(para)

    ner_medical = MedicalNER(".\\model-data\\")
    medical_ner_rslt = ner_medical.test(para)
    medicine = []
    medical_cond = []
    pathogens = []
    for ent in medical_ner_rslt.ents:
        if ent.label_ == "MEDICINE":
            medicine.append(ent.text)
        if ent.label_ == "MEDICALCONDITION":
            medical_cond.append(ent.text)
        if ent.label_ == "PATHOGEN":
            pathogens.append(ent.text)


    ner_custom = CustomNER(".\\model-data\\")
    custom_ner_rslt = ner_custom.test(para)
    names2 = []; doctor = []; date = []; phone = []; address = []; postal_code = []
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

    reg = Regex(para)


    print("NAMES: ", names)
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
    print("POSTAL CODE: ", postal_code, "\n\n\n")

    check = NER_Checking()
    rt = check(names = names, names2 = names2, doctors = reg.findDr(), phones = reg.findPhone(),
               date = date, address = address, amounts = reg.findRupees(), invoices = reg.findInvoice(),
               gst = reg.findGST(), org = organizations, medicines = medicine, MedCond = medical_cond,
               pathogens = pathogens)

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

