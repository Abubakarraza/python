# Enumerate Function

# The enumerate function is a built-in function in python that allows you to loop over a sequence (such as a list, tuple,string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

fruits  = ['apple','banana','mango','strawberry','kiwi']

for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")


# Changing the start index

# By default , the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:
print("Index start with 1")
for index, fruit in enumerate(fruits,start=1):
    print(f"{index}:{fruit}")