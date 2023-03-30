
# Tuples

# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuples items are separated by commas and enclosed within round brackets().Tuples are not changeable meaning we can not alter than after creation of tuple

tup =(1,2,3,4,5,6,7,8,"red",False)

print("type of tuple:",type(tup))

print("tuple",tup)

# All slicing methods are same like list it give us new tuple when we slice tuple

tup2=tup[1:5]
print("tuple2:",tup2)

if 3 in tup:
    print("yes , 3 is present in tuple")

    
# Note: we cannot change tuple ,we cannot change the length of original tuple in tup2 case it give us new tuple the tup remain same,even we cannot change the value of tuple just like string,overall list are immutable and strings are also immutable . list are mutable    