#Type Casting
#Convert one Data type into another Data Type
# For Example i want to add 2 number but it is in the String
a = '1'
b='2'
print("String:",a+b)
# result will be 12 because they are string and python concat it
# If i want to add it as integer so first we convert it into integer using int() predefine function
print("dataType:",int(a) + int(b))
# Now:Result will be 3
#Note: int() is only work for number of String not for text
# Type Casting has two Types
# 1:Explicit Conversion 
# 2:Implicit Conversion 


# 1:Explicit Conversion 

#Explain: The conversion of one data type into another data type dove via developer or Programmer Example Above


# 2:Implicit Conversion


# Explain:The conversion of one data type into another data type vai done by python itself
#Example
c = 9.3
d=2
print("Implicit Data Type",c + d)
#Python convert output result into float Data Type 


# Different Data type Casting in Python
# 1: int (already explain Above)
# 2 : float (convert int into float value)
e = 9
print("float",float(e))
#Result : 9.0
# it also convert string number into float value
f = "2.3"
print("intFloat",float(f))
# Result: 2.3

# 3: Str (convert data into string)
g = 34
g_str = str(g)
print("string:",g_str)
print(type(g_str))