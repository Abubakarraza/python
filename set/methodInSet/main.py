# Set Method 

# Joining set

# Sets in python more or less work in the same way as sets in mathematics. We can perform operation like union and intersection on the sets just like in mathematics

# union() and update()

# The union() and update methods prints a all items that are present in the sets.The union() method return a new set whereases update method add items into the existing set from another set

fruits ={"apple","banana","grapes"}

fruits2={"banana","strawberry","kiwi"}

fruits3=fruits.union(fruits2)

print('fruits:',fruits3)

print(fruits,fruits2)

# in union method result will be save in new variable it can't update old set (example above 👆)

fruits2.update(fruits)
print("fruits2:",fruits2)
# in update method result will be update the fruits2 (example above 👆)
