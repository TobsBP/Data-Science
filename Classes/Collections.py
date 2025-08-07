# Tuples are immutable, so we cannot change them

my_tuple = ('Goku','Vegeta','Trunks','Gohan')

for caracter in my_tuple:
    caracter

my_tuple[1:3] # Slicing the tuple, the last index is not included

my_tuple[2:] # Slicing from index 2 to the end

my_tuple[-2] # Accessing the second last element

len(my_tuple) # Length of the tuple

max(my_tuple) # Maximum value in the tuple

min(my_tuple) # Minimum value in the tuple


# Lists allow full modification, so we can change them

my_list = ['Goku','Vegeta','Trunks','Gohan']

# print(my_list) 

my_list.append('Bulma')  # Adding an item to the end of the list

my_list.insert(1, 'Piccolo')  # Inserting an item at index 1

# print(my_list)

my_list[2] = 'Frieza'  # Changing the value at index 2

my_list.remove('Gohan')  # Removing an item by value

del my_list[0]  # Deleting an item by index


# Collections - Sets are unordered and do not allow duplicate items 

collection = {'Goku','Vegeta','Trunks','Gohan'}

collection.add('Bulma')  # Adding an item to the set

collection.add('Goku')  # Trying to add a duplicate item, will not be added

# print(collection)

collection.remove('Gohan')  # Removing an item by value

# print(collection)


# Dictionaries are collections of key-value pairs

my_dict = {
    'name': 'Goku',
    'age': 43,
    'gender': 'male'
}

my_dict['race'] = 'Saiyan'  # Adding a new key-value pair

my_dict['family'] = ['Chi-Chi', 'Goten', 'Gohan', 'Pan']  # Adding a list as a value

my_dict['age'] = 43  # Changing the value associated with the key 'age'

del my_dict['gender']  # Deleting a key-value pair by key

my_dict['family'][0] # Accessing the first element of the list stored in 'family'