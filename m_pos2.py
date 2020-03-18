import spacy

nlp = spacy.load('en') #Loading the spacy english model
doc = nlp('There are many advantages to identifying entities in a specified phrase.') #Text for creating object, doc

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop) #Viewing the result with different POS attributes

