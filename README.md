# Designation_Detection_using_spaCy_NER

This repository contains a guide and scripts for training a custom Named Entity Recognition (NER) model using spaCy. The model is tailored to recognize specific entities relevant to your data, improving accuracy for specialized use cases.

DATA FORMAT
Ensure your data is formatted in JSON as shown below:

[ ["Text with entity information.", { "entities": [[start, end, "LABEL"]] }], ... ]

STEPS TO TRAIN SPACY MODEL
Download base_config.cfg file from spacy documentation and save it in the same folder where you have code to train NER. Here we have a base_config.cfg file. You can use this file. Just set path of train and test.spacy files in the base_config.cfg file

First run

''' python main.py '''
RUN this command

