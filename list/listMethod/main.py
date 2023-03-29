# Methods of List

lst = [50,11,1,56,2,9,4,5,6]
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