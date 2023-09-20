# Importing all the required modules
import json
from spacy.tokens import DocBin
from spacy import blank, load
from tqdm import tqdm
from spacy.util import filter_spans


class MedicalNER:

    """ This Custom Medical NER trained on Medical Dataset is build to identify Medical terminology
    from a string, and the labels it can identify is Medicine, Medical Condition & Pathogens."""

    def __init__(self, path, filename = "Corona2.json"):
        self.filepath = path
        with open(self.filepath + filename, 'r') as f:
            self.data = json.load(f)

    def organizeDataset(self):

        """ Extracting the important informations from the dataset like the text, annotations and
         storing them in a Python list with the help Python dictionary."""

        training_data = []
        for example in self.data['examples']:
            temp_dict = {'text': example['content'], 'entities': []}

            for annotation in example['annotations']:
                start = annotation['start']
                end = annotation['end']
                label = annotation['tag_name'].upper()
                temp_dict['entities'].append((start, end, label))

            training_data.append(temp_dict)

        # print(training_data[0]['text'][104:112])
        return training_data

    def organizeToTrain(self, td):

        """ Organizing the list dataset into required .spacy format so that the model can access the
        data inside the dataset and train them. """

        # Load a new spacy model
        nlp = blank("en")
        doc_bin = DocBin()

        for training_example in tqdm(td):
            text = training_example['text']
            labels = training_example['entities']
            doc = nlp.make_doc(text)
            ents = []

            for start, end, label in labels:
                span = doc.char_span(start, end, label = label, alignment_mode = "contract")
                if span is None:
                    print("Skipping entity")
                else:
                    ents.append(span)
            filtered_ents = filter_spans(ents)
            doc.ents = filtered_ents
            doc_bin.add(doc)

        doc_bin.to_disk(self.filepath + "trainMedical.spacy")
        return nlp, doc_bin

    def train(self):
        """ Command to train the dataset. This code is implemented in the terminal. """
        pass
        # python -m spacy download en_core_web_lg
        # python -m spacy init fill-config base_config.cfg config.cfg
        # python -m spacy train config.cfg --output ./ --paths.train ./model-data/trainMedical.spacy
        # --paths.dev ./model-data/trainMedical.spacy

    def test(self, string):

        """ Loads the already trained model stored in the directory, and tries to get the required entities
         and return them. """

        nlp_ner = load(self.filepath + "model-best-medical")
        doc = nlp_ner(string)
        with open(self.filepath + "labelMedical_.txt", "w") as fp:
            for ent in doc.ents:
                fp.write(ent.text + "\t| " + ent.label_ + "\n")

        print("Medical NER called, and it has returned the extracted values...")
        return doc

    def __call__(self, *args, **kwargs):
        # trainData = self.organizeDataset()
        # print(trainData)
        # nlp, doc_bin = self.organizeToTrain(trainData)
        return self.test(kwargs['string'])

    def __del__(self):
        pass
