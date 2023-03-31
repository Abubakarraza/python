# f-String

# History:
# old method

# string formatting can be done in  python using format method 
name = "Hello my name is {} and i am a {}"
# first argument in format place in first curly braces and so on

print(name.format("Abubakar","software developer"))

# if i pass profession first it will display profession in the field of name just like that

print(name.format("software developer","Abubakar"))
# you can solve this issue by passing number like 👇
fullName = "Hello my firstname is  {1} and my second name is  {0}"
print(fullName.format("Raza","Abubakar"))
# This will solve the problem but this is not solution to because if we have more than 10 value to format in the string it is difficult to handle the hierarchy of it



# But here python solve our problem using f string where you pass variable (just like template literals in javascript)

# F-string

# It is a new string formatting mechanism introduced by the PEP 498. It is also known as literal string Interpolation or more commonly as f-string .(f character proceeding the string literal). The primary focus of this mechanism is to make the interpolation easier.


# Example 

profession = "Software developer"
age = 19
myName = "Abubakar Raza"
about = f"Hello , my name is {myName},i am {age} year old and i am {profession}"

print(about)

# we can also do multiple task using f-string one more example 👇
num1 = 12
num2 = 10

print(f"product of {num1} and {num2} is {num1 * num2}")