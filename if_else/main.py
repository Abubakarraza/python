# if else statement


# First Example
age = int(input("Please type your age:"))
if(age >= 18):
    print("You can drive")
else:
    print("You cannot drive")


# Second Example
num = int(input("Please Enter any number:"))
if(num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is zero") 
else:
    print("Number is Positive")            

# Nested IF else statement

number = int(input("Please Enter any Number:"))
if(number < 0):
    print("Number is negative")
elif (number > 0):
    if(number > 0 and number <= 10):
        print("Number is in between 1-10")
    elif(number > 10 and number <= 20):
        print("Number is in between 11 -20")
    else:
        print("Number is greater than 20")        
else:
    print("Number is zero") 
       