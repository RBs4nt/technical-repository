import spacy

string = "Apple, one of the world's largest electronics manufacturers, is based in California, USA, and is valued at $ 1,331 trillion."
nlp = spacy.load('en')
ent = nlp(string)

for ents in ent.ents:
    print(ents.text, ents.label_)
    
