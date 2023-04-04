# Dictionary

# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets{}

info = {
    'name':'Abubakar Raza 😎',
    "age" :18,
    "developer":True
}
print(info)

# Accessing Dictionary items:

# Accessing single values:

# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.


print("name:",info["name"])

# Accessing values using get

print("age:",info.get("age"))

# The difference between key access and get is that 🤷‍♂️ key access throw error if value is not found in corresponding key but in get case it give none 👀 if key is not found in dict


# Accessing multiple values:

# We can print all the values in the dictionary using values() method.

# it return list of values 👇

print("values:",info.values())

# Accessing keys

# We can print all the keys in the dictionary using keys() method.

# it also return list of keys 👇

print("keys:",info.keys())


# Accessing key-value pairs:

# We can print all the key-value pairs in the dictionary using items() method 


# it return tuple of key value pair

print("items:",info.items())


# Accessing item using loop 

for key, value in info.items():
    print(f"The value of {key} is {value}")