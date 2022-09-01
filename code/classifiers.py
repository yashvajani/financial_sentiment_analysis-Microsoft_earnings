from transformers import BertTokenizer, BertForSequenceClassification
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
from sklearn import preprocessing
import torch
class classify():
    '''
    This function contanins all the classifiers used in the sentiment analysis pipeline
    bert_classifier = The FinBERT classifier lablled BERT1 in the accompanying analysis
    bert_classifier_2 = The FinBERT classifier lablled BERT2 in the accompanying analysis
    roberta_classifier = The RoBERTa classifier lablled RoBERTa in the accompanying analysis

    This function applies the specified classifier on text data
    This is used to classify the text data obtained after the pre-processing steps labelled 'text_clean'
    '''
    def bert_classifier(self, text):
        '''
        More details about the classifier are available at: https://huggingface.co/yiyanghkust/finbert-tone
        '''
        finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3, from_tf=True)
        tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
        nlp = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer)

        sentences = text
        results = nlp(sentences)
        return results

    def bert_classifier_2(self, text):
        '''
        More details about the classifier are available at: https://huggingface.co/ProsusAI/finbert
        '''
        tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
        model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

        inputs = tokenizer(text, padding = True, truncation = True, return_tensors='pt')
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return predictions

    def roberta_classifier(self, text):
        '''
        More details about the classifier are available at: https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis
        '''
        tokenizer = AutoTokenizer.from_pretrained("mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
        model = AutoModelForSequenceClassification.from_pretrained("mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

        inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
        outputs = model(**inputs)
        predictions = outputs.logits.detach().numpy()
        min_max_scaler = preprocessing.MinMaxScaler()
        predictions = min_max_scaler.fit_transform(predictions)
        return predictions
