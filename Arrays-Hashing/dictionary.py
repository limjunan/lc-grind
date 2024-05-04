# Python dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Useful techniques in dictionaries

# 1. Getting a value by key
value = dict1.get('a')  # Returns 1

# 2. Adding a key-value pair
dict1['f'] = 6

# 3. Removing a key-value pair
del dict1['f']

# 4. Iterating over keys
for key in dict1.keys():
    print(key)

# 5. Iterating over values
for value in dict1.values():
    print(value)

# 6. Iterating over key-value pairs
for key, value in dict1.items():
    print(key, value)

# 7. Checking if a key exists
if 'a' in dict1:
    print('Key exists')

# 8. Merging two dictionaries
dict2 = {'f': 6, 'g': 7}
dict1.update(dict2)

# Useful techniques

# 1. Dictionary comprehension to create a dictionary
squares = {i: i**2 for i in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2. map() - apply a function to all the values of a dictionary
# Note: map() returns an iterator, so we convert it to a list
squares_map = list(map(lambda x: x**2, dict1.values()))

# 3. filter() - filter values of a dictionary
# Note: filter() returns an iterator, so we convert it to a list
even = list(filter(lambda x: x % 2 == 0, dict1.values()))

# 4. Converting an array into dictionary with index as value
arr = ['a', 'b', 'c', 'd', 'e']
dict1 = {item: index for index, item in enumerate(arr)}

# For duplicate values in the array
for index, item in enumerate(arr):
    if item in dict1:
        dict1[item].append(index)
    else:
        dict1[item] = [index]