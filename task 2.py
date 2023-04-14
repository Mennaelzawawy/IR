import nltk
x=input("Enter text:")
print("1.print tokenized words \n2.print tokenized sentences \n3.print text")
y=int(input('select a number:'))
if y==1:
    print(nltk.word_tokenize(x))
elif y==2:
    print(nltk.sent_tokenize(x))
elif y==3:
    print(x)

