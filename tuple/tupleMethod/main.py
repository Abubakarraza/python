# Manipulating Tuple

# Tuples are immutable . hence if you want to remove ,add and change the items of tuple. then first must you convert tuple into list.Then perform operation on that list and convert back into tuple.

countries = ("pakistan","saudi arabia","dubai","oman","turkey","qatar",'tes')
print("before:",countries)
lst = list(countries)
lst.append("india")
lst.pop(len(lst)-2)
lst[2]="UAE"
countries = tuple(lst)
print("after",countries)


# However, we can directly concatenate two tuple without converting them into list because we create new tuple
tup1=(1,2,3)
tup2=(4,5,6)
tup3=tup1 + tup2
print("final Tuple:",tup3)

# Count

# The count method of tuple return the number of items present in tuple

tup4 =(1,2,1,4,5,1)
print("count:",tup4.count(1))


# index 

# This method return the index of the first occurrence of the list item
#syntax: index(element,start,end)
# start and end is used to define the specific part of tuple it only check in this part start and end are optional(start and end is in index)
# Note : if ele is not exist in tuple , tuple throw error

print("index:",tup4.index(1))

# len()
# we get the length of tuple using len()

print("length of tuple:",len(tup4))