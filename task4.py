def hash_key(v,m):
    return v%m
m=7
x=int(input('Enter a value:'))
print('hash key of entered value is:',hash_key(x,m))