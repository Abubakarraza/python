name = "Abubakar"
# it will print my name with character because name is also a list
for i in name:
    print(i)


# print list using loop     
colors = ["green","yellow","brown","red","blue"]
for color in colors:
    print(color)
    if(color == "blue"):
        print("This is my favorite color")    


# Print 1 - 100 number using for loop
# In this code i used range it take two param start and end 
for i in range(1,100):
    print(i+1)


# In this code snippet i also used third argument which is step
# it means it add step value to start value at every time
for i in range(1,10,2):
    print(i)