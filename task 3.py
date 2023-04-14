from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
ps=PorterStemmer()
snw=SnowballStemmer
x=input("Enter text:")
print("1.print tokenized words \n2.print tokenized sentences \n3.print text \n4.stemming")
y=int(input('select a number:'))
if y==1:
    print(word_tokenize(x))
elif y==2:
    print(sent_tokenize(x))
elif y==3:
    print(x)
elif y==4:
    print('1.porter stemmer \n2.snowball stemmer')
    z=int(input('Choose a number:'))
    if z==1:
        print(ps.stem(x))
    elif z==2:
        print(snw.stem(x))