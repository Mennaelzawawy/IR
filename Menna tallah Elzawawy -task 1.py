Doc_1="new home sales top forecasts"
Doc_2="home sales rise in july"
Doc_3="increase in home sales in july"
Doc_4='july new home sales rise'
docs=[Doc_1,Doc_2,Doc_3,Doc_4]


x =input("Enter the term:")
for i,doc in enumerate(docs):
    for term in doc.split():
        if x == term:
            print(x,"in",i+1)
