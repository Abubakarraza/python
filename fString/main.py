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