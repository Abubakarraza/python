# List comprehension is used for creating new list from other iterable like list,tuple,dictionary,sets , even in array and string


# Syntax
# List = [Expression(item) for item in iterable if condition]

# Expression : It is the item which is being iterated

# Iterable : it can be list tuple ,sets, dictionary ,even in array and string

# Condition : condition check if the item should be added to the new list or not

# Example# 1 :

lst=[i for i in range(5)]
print(lst)


# Example# 2 :
lst1=[i*i for i in range(20) if i % 2 == 0]
# it will all  print even number
print(lst1)