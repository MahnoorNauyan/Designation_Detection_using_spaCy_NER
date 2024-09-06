import spacy

trained_model = spacy.load("models/outpu/model-best")
text = "Jhon is a Software Engineer. His brother is the Physician in the city hospital. Ali works as a Data Scientist at Google."
doc = trained_model(text)

for ent in doc.ents:
    print(f"Detected Entity: {ent.text} , Label:{ent.label_}")
