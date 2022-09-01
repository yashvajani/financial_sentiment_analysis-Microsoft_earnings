# %% Creating a function to process extracted text
'''
The function below extracts textual data from microsoft earnings reports in the 
specified working directory and stores it in a dataframe with corresponding information 
about the sentence position in the text
'''
import re
import spacy
from nltk.stem import WordNetLemmatizer
#nltk.download('wordnet')
#nltk.download('omw-1.4')
class TextProcessor():
    def preprocess_text(self, text, lower, remove_unicode, lemmatize, remove_stops):
        '''
        lower = 'True' to lower the text, 'False' otherwise
        remove_unicode = 'True' to remove unicode data from the text, 'False' otherwise
        lemmatize = 'True' to lemmatize the text, 'False' otherwise
        remove_stops = 'True' to remove stopwords from the text, 'False' otherwise

        This is a function to pre-process text data
        '''
        nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner', 'tagger', 'tok2vec'])
        english_stops = nlp.Defaults.stop_words
        
        lemmatizer = WordNetLemmatizer()

        if lower == True:
            text = ' '.join([word.lower() for word in text.split()])
        
        if remove_unicode == True:
            text = re.sub(r'[^\x00-\x7F]', '', text)

        if lemmatize == True:
            text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

        if remove_stops == True:
            text = ' '.join([w for w in text.split() if w not in english_stops])

        return text