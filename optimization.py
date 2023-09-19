# Importing all the required modules
import re
from similarity.cosine_match import CosineSimilarity
class NER_Checking:
    """ Code to get the most suitable output from our NERs outputs. """
    def __init__(self):
        self.finalEntity = {}

    @staticmethod
    def is_valid_address(address):
        # Example: Names must contain at least one alphabetical character
        temp = []
        for char in address:
            if re.match(r'[a-zA-Z0-9,.\-]', char) is not None:
                temp.append(char)
        return temp

    @staticmethod
    def is_valid_medicine(medicine):
        # Example: Medicines should not contain numbers
        return not any(char.isdigit() for char in medicine)

    @staticmethod
    def is_valid_condition(condition):
        # Example: Conditions should not contain numbers
        for char in condition:
            if len(char.split()) > 1:
                condition.remove(char)
        return condition

    @staticmethod
    def is_valid_invoice(invoice):
        # Example: Conditions should be of max length
        i = [len(char) for char in invoice]
        return invoice[i.index(max(i))]

    @staticmethod
    def is_valid_amount(amount):
        # Example: Conditions should be of max length and shouldn't contain other that R/S/r/s/./,
        test = []
        for char in amount:
            if char.isnumeric():
                test.append(char)
            else:
                x = ""
                flag = 0
                for i in char:
                    if i.isdigit():
                        x = x + i
                    elif i != "R" or i != "r" or i != "S" or i != "s" or i != "," or i != "." or i != "`":
                        flag = 1
                        break
                if flag == 0:
                    test.append(x)
        i = [len(char) for char in test]
        try:
            return test[i.index(max(i))]
        except ValueError:
            return -1

    @staticmethod
    def is_any_specialChar(input):
        # Example: Conditions to check is there any special character in the string
        for char in input:
            if not bool(re.search(r'[a-zA-Z0-9,.\-]', char)):
                input.remove(char)
        return input

    @staticmethod
    def is_valid_date(dates):
        for char in dates:
            if re.search(r'[^a-zA-Z0-9,.\-\s\\]', char) is not None:
                dates.remove(char)
        return dates

    @staticmethod
    def valid_number(numbers):
        # Use list comprehension to filter out strings with numbers
        filtered_list = [item for item in numbers if not any(char.isdigit() for char in item)]
        return filtered_list

    @staticmethod
    def is_valid_doctor(doctors):
        for doctor in doctors:
            if len(doctor.split()) >= 3:
                return doctor
        return -1

    @staticmethod
    def is_valid_phone(phones):
        for phone in phones:
            if 10 <= len(phone) <= 13:
                return phone
        return -1

    @staticmethod
    def is_valid_gst(gsts):
        temp = gsts[0]
        for gst in gsts:
            if len(gst) == 15:
                return gst
            elif 15 <= len(gst) >= 16:
                temp = gst
        return temp

    def __call__(self, *args, **kwargs):

        # Patient Name
        minVal = 100
        try:
            minName = kwargs['names'][0]
            for name in kwargs['names']:
                for doctor in kwargs['doctors']:
                    scr = CosineSimilarity().score(name, doctor)
                    if scr < minVal:
                        minVal = scr
                        minName = name
        except IndexError:
            minName = ""
        self.finalEntity['name'] = minName

        # Doctor Name
        if len(kwargs['doctors']) > 1:
            self.finalEntity['doctor'] = self.is_valid_doctor(kwargs['doctors'])
        else:
            self.finalEntity['doctor'] = kwargs['doctors'][0]

        # Phone Number
        if len(kwargs['phones']) > 1:
            self.finalEntity['phone'] = self.is_valid_phone(kwargs['phones'])
        else:
            self.finalEntity['phone'] = kwargs['phones'][0]

        # Date
        if len(kwargs['date']) > 1:
            self.finalEntity['date'] = self.is_valid_date(kwargs['date'])[0]
        else:
            self.finalEntity['date'] = kwargs['date'][0]

        # Address
        if len(kwargs['address']) > 1:
            self.finalEntity['address'] = self.is_valid_address(self.is_any_specialChar(kwargs['address']))[0]
        else:
            self.finalEntity['address'] = kwargs['address']

        # Amount
        if len(kwargs['amounts']) > 1:
            self.finalEntity['amount'] = self.is_valid_amount(kwargs['amounts'])
        else:
            self.finalEntity['amount'] = kwargs['amounts'][0]

        # Invoice Number
        if len(kwargs['invoices']) > 1:
            self.finalEntity['invoice'] = self.is_valid_invoice(kwargs['invoices'])
        else:
            self.finalEntity['invoice'] = kwargs['invoices'][0]

        # GST Number
        if len(kwargs['gst']) > 1 or kwargs['gst']:
            self.finalEntity['gst'] = self.is_valid_gst(kwargs['gst'])
        else:
            self.finalEntity['gst'] = kwargs['gst']

        # Organizations
        if len(kwargs['org']) > 1:
            self.finalEntity['org'] = list(set(kwargs['org']))[0]
        else:
            self.finalEntity['org'] = kwargs['org']

        # Medicines, Medical Conditions & Pathogens
        for med in kwargs['medicines']:
            for name in kwargs['names'] + kwargs['names2']:
                if CosineSimilarity().score(med, name) > 70:
                    kwargs['medicines'].remove(med)

        self.finalEntity['medicines'] = kwargs['medicines']

        if len(kwargs['MedCond']) > 1:
            self.finalEntity['MedCond'] = list(set(self.is_valid_condition(self.valid_number(self.is_any_specialChar(kwargs['MedCond'])))))
        else:
            self.finalEntity['MedCond'] = kwargs['MedCond']
        self.finalEntity['pathogens'] = [pathogen for pathogen in kwargs['pathogens'] if not pathogen.isnumeric()]

        return self.finalEntity

    def __del__(self):
        pass