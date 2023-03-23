# There  are four types of argument in python that we can provide in function
# 1: Default Argument
# 2: Keyword Argument
# 3: Required Argument
# 4: Variable length Argument

# 1: Default Argument Function 
# You can provide a default argument value while creating function. This way the function assumes a default value even if a value is not provided in the function call for that argument if the value is provided the given value is overwrite by default value

def name(fName,sName="Raza",lName="Ansari"):
    print(fName,sName,lName)
name("Abubakar")
# Now value is overwrite
name("Abubakar","")


# 2: keyword Argument
# We can provide argument with key = value the interpreter recognize the argument by the parameter name. Hence the order in which the argument are passed does not mattere 
def average(a=10,b=5):
    print("The average of ",a,"and",b,"is",(a+b)/2)
average()
# Now in this the order is different in function but result is same
average(b=56,a=89)


# 3: Required Argument
# In case we don't pass the argument with a key = value syntax, then it is necessary to pass the argument in the correct positional order and the number of argument passed should match with actual function definition.


def multiplication(a,b,c):
    print(a * b * c)
# In that case all argument is Required
multiplication(1,2,3)    


# 4: Keyword Arbitrary Argument
# While creating the function ,pass a * before the parameter name while defining the function . The function access the argument by processing in the form of dictionary
# * as tuple 
# ** as dictionary
# Example:


def averageNum(*numbers):
    print(type(numbers))
    sum = 0
    for number in numbers:
        sum=sum + number
    print("Average of number is ",sum/len(numbers))    


averageNum(1,2)    

def fullName(**name):
    print(type(name))
    print(name["fname"],name['lname'])
fullName(fname="Abubakar",lname="Raza")