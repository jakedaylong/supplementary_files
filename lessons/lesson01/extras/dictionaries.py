"""info from https://www.geeksforgeeks.org/python-dictionary/
Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a ‘comma’.

A Dictionary in Python works similar to the Dictionary in a real world. Keys of a Dictionary must be unique and of immutable data type such as Strings, Integers and tuples, but the key-values can be repeated and be of any type."""

my_customers = [
    ('01',
     'XYZ abc',
     42.09,
     ),
    ('02',
     'TR deep',
     90.01
     )
]


my_other_customers = [
    {'ID': '01',
     'Name': 'XYZ abc',
     'Credit': 42.09
     },
    {'ID': '02',
     'Name': 'TR deep',
     'Credit': 90.01
     }
]

for customer in my_other_customers:
    print(customer['Name'])

# OR

for customer in my_other_customers:
    print(customer.get('Name'))


for customer in my_other_customers:
    customer['Credit'] *= 1.5


for customer in my_other_customers:
    print(customer.values())


for customer in my_other_customers:
    for name, value in customer.items():
        print(name, value)

# see https://www.w3schools.com/python/python_dictionaries.asp


