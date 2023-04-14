import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
data=pd.read_csv('heart_disease.csv')
ps=PorterStemmer()
snw=SnowballStemmer
stop_words=stopwords.words('english')
word_tokenize=word_tokenize(data)
new_data=[]
for i in word_tokenize:
    if i not in stop_words:
        new_data.append(i)
port_stem=PorterStemmer(new_data)
snow_stem=SnowballStemmer(new_data)


    



