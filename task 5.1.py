value_list = [3, 2, 9, 11, 7]
print('1. Construct whole hash table')
hash_table = {}
def hash_key(v, m):
    return v % m
if int(input('Enter num 1 to construct hash table: ')) == 1:
    for v in value_list:
        key = hash_key(v, len(value_list))
        if key in hash_table:
            hash_table[key].append(v)
        else:
            hash_table[key] = [v]
    print(hash_table)
while True:
    operation = int(input('2. Add new element to hash table\n3. Update value of a key\n4. Delete an element from hash table\n5. Search for an element\n6. Print all elements in hash table with keys\nChoose another number to perform an operation: '))
    if operation == 2:
        value = int(input('Enter a value: '))
        key = hash_key(value, len(hash_table) + 1)
        if key in hash_table:
            hash_table[key].append(value)
        else:
            hash_table[key] = [value]
        print('Updated hash table:', hash_table)
    elif operation == 3:
        key = int(input('Enter a key: '))
        value = int(input('Enter a value: '))
        if key in hash_table:
            hash_table[key].append(value)
        else:
            hash_table[key] = [value]
        print('Updated hash table:', hash_table)
    elif operation == 4:
        key = int(input('Enter a key you want to delete: '))
        if key in hash_table:
            del hash_table[key]
        print('Updated hash table:', hash_table)
    elif operation == 5:
        key = int(input('Enter a key you want to search for: '))
        if key in hash_table:
            print('Values of entered key are:', hash_table[key])
        else:
            print('Value is not found. Try to enter a proper key.')
    elif operation == 6:
        print(hash_table)