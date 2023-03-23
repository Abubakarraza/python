# The function is a block of code that perform a specific task whenever it is called
# There are two types of function in python 
# 1: Built in function 
# 2: User define function


# Built in function 

# These function are defined and pre coded in python. some example of built in function are as follow
# for example : int(),str(),upper(),lower(),max(),len(),dic(),print() etc


# User Define function

# We can create function in python specific tasks as per our needs . Such function are called User defined function
def addNumber(a , b):
    print("The Sum of ", a, "+",b,"is",a + b)    
addNumber(3 , 5)
def calculateGMean(a,b):
    Mean = (a * b)/(a + b)
    print("The mean of ",a ,"and", b ,"is",Mean)
calculateGMean(4,8)    
def isGreater(a,b):
    if(a>b):
        print(a,"is greater than",b)
    else:
        print(a,"is less than or equal to",b)    
isGreater(9,5)  



# Return Statement
# The return statement is used to return the value of the expression back to the calling function 


def getFullName(fName,sName,lName):
    fullName= fName +" "+ sName +" " + lName
    return fullName
fullName = getFullName("Abubakar","Raza","Ansari")
print("fullName:",fullName)