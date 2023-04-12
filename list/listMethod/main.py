# Methods of List

lst = [50,11,1,56,2,9,4,5,1,6]
print("list:",lst)
# Append

# Append will add the element at the end of list (just like push in js) it will update the original list
lst.append(7)
print("append List:",lst)


# Sort

# This method sort the list in ascending order.The original list is updated

lst.sort()
print("Sorted List:",lst)

# if i pass reverse True in sort param it will sort list in descending order

lst.sort(reverse=True)
print("Reverse Sorted:",lst)


# reverse 

# This method reverse the order of list

lst.reverse()
fruits = ["apple","banana","pineapple","strawberry"]
fruits.reverse()
print("reverse List:",lst)
print("reverse fruits:",fruits)

# index

# This method return the index of the first occurrence of the list item

print("index of 11 is",lst.index(11))


# count 

# Return the count of the number of items with the given value

print("Count of 1 is :",lst.count(1))


# copy 

# Return the copy of list . This can be done to perform operation on the list without modifying  the original list.

newList=lst.copy()
newList[0]=0
print("Original List:",lst)
print("newList:",newList)  


# insert 

# This method insert an item at the given index,User has to specify index and item to be inserted within the insert method
# Syntax: insert(index,item)

lst.insert(0,0)
print("insert item:",lst)


# extend

# This method adds an entire list or any other collection datatype(set,tuple,dictionary) to the existing list. it will add items at the end of the list
l=[100,200,300]
lst.extend(l)
print(lst)


# Concat two list

# you can simply concatenate two list to join two list
a =[1,2,3,4]
b = [5,6,7,8]
c = a + b
print("Concat list:",c)


# Pop 

# Pop remove item from list in pop method we pass the index of item it is removed from list   if you did not pass any index it remove item from the end of list
print("Before Pop:",a)
a.pop(3)
print("After Pop:",a)