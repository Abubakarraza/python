# Lists are ordered collection of data items.
# They Store multiple items in a single variable
# List items are separated by commas and enclosed within square brackets []
# Lists are changeable meaning we can alter them after creation
list1=[1,2,3,4,5,6,7,8]
list2=["Red","Green",'Blue']
print(list1)
print(list2)
# we can also pass multiple type of variable in list
list3=[1,"Red",True]
print(list3)

# Accessing List Items
# Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index 0,second item has 1 and third item has 3 and so on.
print(list2[1])
print(list3[2])

# We can also access list item using negative index . when we access item using -ve index it start from the end of list    Note -ve index is start from -1
print(list1[-1])



# We can check if a given item is present in the list. This is done using the in keyword
# Same thing apply for string as well
if 8 in list1:
    print("Yes it is exist")
else:
    print("No it is found")    



# Printing element with a particular range
# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range
# list[start:end(optional):jump(optional)]


print(list2[1:])
# In this case it take elem from 1 index to the length of list


print(list1[2:7])
# Note : it pick start index ele but not last index ele