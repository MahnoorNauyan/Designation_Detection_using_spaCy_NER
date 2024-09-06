# imports
import spacy
from spacy.tokens import DocBin
from spacy.util import filter_spans
import json
from pathlib import Path

# Loading data
train_data = json.load(open("train.json"))
test_data = json.load(open("train.json"))

# preparing data in binary format(spaCy)
# Create blank space pipeline


def data_spacy_format(train_data, output_file):
    nlp = spacy.blank("en")
    docbin = DocBin()
    for text, ents in train_data:
        doc = nlp.make_doc(text)  # building Sapcy doc
        temp_dict = []  # Initialize a temporary list to store spans
        for start, end, label in ents["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")

            if span is None:
                print("None is returned.")

            else:
                temp_dict.append(span)
        # print(temp_dict) #Uncomment to check designations

        doc.ents = filter_spans(
            temp_dict
        )  # to remove overlapping entities using filterspan
        docbin.add(doc)  # Add this doc in DocBin()
    docbin.to_disk(output_file)


output_path_train = "train.spacy"
output_path_test = "test.spacy"
data_spacy_format(train_data, output_path_train)
data_spacy_format(test_data, output_path_test)
