# Importing the required Python Regular Expression (Regex) module
import re

class Regex:

    """ This is a part of our NER system which use Regular Expression to find Entities from the string.
     We have written our own Regular Expression to find, Phone No., Invoice No., GST, Names with Dr.,
     and Amounts (in Rs). """

    def __init__(self, text):
        self.text = text

    def findPhone(self):

        # regular expression pattern to match phone numbers
        phone_pattern = r'\(?\d{3}\)?[-\s]?\d{3}[-.\s]?\d{4}(?:\d{1,2})?'

        # Find all phone numbers in the text
        phone_numbers = re.findall(phone_pattern, self.text)

        # Checks weather the number is of length 10-12 or not, if it's more than that, its get popped out
        for number in range(len(phone_numbers)):
            try:
                x = self.text.find(phone_numbers[number])
                if self.text[x + len(phone_numbers[number])].isdigit():
                    phone_numbers.pop(number)
            except IndexError:
                pass

        # If found any phone number, then returns the list, otherwise 0
        if len(phone_numbers) > 0:
            print("Regex called, and it has returned the extracted Phone No...")
            return phone_numbers
        return []

    def findInvoice(self):

        # Regular expression pattern to match invoice numbers
        invoice_pattern = r'(?i)(?:invoice\s*number|invoice|invoice\s*#\s*|#)\s*([a-zA-Z0-9-]+)'

        # Find all invoice numbers in the text
        invoice_numbers = re.findall(invoice_pattern, self.text, re.IGNORECASE)

        # If found any invoice number, then returns the list, otherwise 0
        if len(invoice_numbers) > 0:
            print("Regex called, and it has returned the extracted Invoice No...")
            return invoice_numbers
        return []

    def findGST(self):

        # Regular expression pattern to match Indian GST numbers
        gst_pattern = r'[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]'

        # Find all GST numbers in the text
        gst_numbers = re.findall(gst_pattern, self.text)

        # If found any gst number, then returns the list, otherwise 0
        if len(gst_numbers) > 0:
            print("Regex called, and it has returned the extracted GST No...")
            return gst_numbers
        return []

    def findDr(self):

        # Regular expression pattern to match names starting with "Dr."
        dr_name_pattern = r'\bDr\.\s+[A-Z][a-zA-Z]+\s+[A-Z][a-zA-Z]+\b'

        # Find all names starting with "Dr." in the text
        dr_names = re.findall(dr_name_pattern, self.text)

        # If found any Doctor, then returns the list, otherwise 0
        if len(dr_names) > 0:
            print("Regex called, and it has returned the extracted Doctors Name...")
            return dr_names
        return []

    def findRupees(self):

        # Regular expression pattern to match rupee amounts
        rupee_amount_pattern = r'(?i)(?:₹|rs|rupees?)\s*([\d,]+(?:\.\d{1,2})?)'

        # Find all rupee amounts in the text
        rupee_amounts = re.findall(rupee_amount_pattern, self.text)

        # If found any rupees, then returns the max element from the list, otherwise 0
        if len(rupee_amounts) > 0:
            print("Regex called, and it has returned the extracted Amount (in Rs.)...")
            return rupee_amounts
        return []

    def __call__(self, *args, **kwargs):
        pass

    def __del__(self):
        pass
