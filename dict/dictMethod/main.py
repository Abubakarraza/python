# Method in dictionary

# Dictionary uses several built-in-method for manipulation. They are listed below 

info={
    "name":"Abubakar Raza",
     "age":18,
     "developer":True
}

# update()

# The update() method updates the values of the key provided to it if the item already exist in the dictionary , else it creates a new key-value pair.😀


info.update({'age':19,"goal":"AI","birthMonth":"june","test":"demo"})

print("info after update:",info)


# Removing items from dictionary

# There are a few methods that we can use to remove items from dictionary

# pop()

# The pop() method removes the key-value pair whose key is passed as parameter
info.pop("test")
print("info after pop:",info)

# popItem()

# The popitem() method removes the last key-value pair from the dictionary.


info.popitem()

print("info after popItem:",info)
# clear()

# The clear() method removes all the items from the list

# info.clear()

# it will clear all the items in dictionary😮

# for now i comment it because i need to used in other method 😀

print("info after clear:",info)


# del()

# we can also use the del keyword to remove a dictionary item.

del info["age"]

print("info after del age:",info)

# Note : if key is not provided , then the del keyword will delete the dictionary entirely

del info 
 
print("info after del:",info) 
# it give us error