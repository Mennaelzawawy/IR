value_list=[3,2,9,11,7]
print('1.construct whole hash table')
dict={}
x=int(input('Enter num 1 to construct hash table :'))
def hash_key(v,m):
    return v%m
if x==1:
    for y in value_list:
        v=hash_key(y,len(value_list))
        dict[y]=v
    print(dict.items())
    z=int(input('2.add new element to hash table\n3.update value of a key\n4.Delete an element from hash table\n5.search for an element\n6.print all elements in hash table with keys \nchoose another number to perform an operation:'))
    if z==2:
        a=int(input('Enter a value:'))
        z=hash_key(a,len(value_list)+1)
        dict[a]=z
        print('Updated dic:',dict)
    elif z==3:
        b=int(input('Enter a key:'))
        c=int(input('Enter a value:'))
        dict.update({b:c})
        print('Updated dic:',dict)
    elif z==4:
        i=int(input('Enter a key you want to delete:'))
        del dict[i]
        print('Updated dic:',dict)
    elif z==5:
        w=int(input('Enter a key you want to search for:'))
        if w in dict:
            print('value of entered key is :',dict[w])
        else:
            print('Value is not found,try to Enter a proper key')
    elif z==6:
        print(dict.items())

    

