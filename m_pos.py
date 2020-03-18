import spacy

nlp = spacy.load('en') #Loading the spacy english model
doc = nlp('Techniques for marking parts of a text.') #Text for creating object, doc

for token in doc:
    print(token.text, token.pos_) #Displays the text and its POS markup
