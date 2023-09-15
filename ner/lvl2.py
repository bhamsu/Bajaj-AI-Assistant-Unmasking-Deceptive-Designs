# Importing all the required modules
import spacy

class BasicNER:
    """ This class is responsible to load the pre-trained large model by spaCy, and tries to get
     the entities especially names and organizations."""

    def __init__(self):
        # self.text = text
        # Load the spaCy large English NER model
        self.nlp = spacy.load("en_core_web_lg")

    def test(self, text):

        # Process the text with spaCy
        doc = self.nlp(text)

        # Extract names (person entities) and organizations
        names = []
        organizations = []
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                names.append(ent.text)
            elif ent.label_ == "ORG":
                organizations.append(ent.text)

        # Print the extracted names and organizations
        # print("Names:", names)
        # print("Organizations:", organizations)

        return names, organizations

    def __call__(self, *args, **kwargs):
        pass

    def __del__(self):
        pass
