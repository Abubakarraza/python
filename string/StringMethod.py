#Strings are immutable you cant change string but you create new string with updated string
a = 'Abubakar !!'
print("Actual String",a)


# you can find the length of string using len() function
print("length Of String :",len(a))


# you can convert string into upperCase and lowerCase using upper and lower respectively 
# Note : it can't update old string it give you new string which you can save in variable use then later
# this note is applicable in all string methods

# For Upper Case 
print("UpperCase String : ",a.upper())
# For Lower Case
print("Lower Case String :",a.lower())

# you can remove trailing character in string using rstrip method it only strip last
print("Remove Trailing Character :",a.rstrip("!"))

# You can replace string with replace method
# The replace method replace all occurrences of a string with another string
print("Replace Abubakar with Raza :",a.replace("Abubakar","Raza") )

# split method return string into list(Array)
# you can pass anything inside param where you want to split you string in below i pass empty space it will split my string where space is exist
print("list of String :",a.split(" "))

# you can capitalize string using capitalize
# The Capitalize method turn only first character of string into upperCase and rest of characters into lowerCase 
blog ="hello this Is the Basic learning of String"
print("Capitalize String :",blog.capitalize())


# center method align the string to the center as per parameter given by the user
print("length of Blog :",len(blog))
print(len(blog.center(100)))
print(blog.center(100))


# count method return the number of time the given value has occurred in string

demo = "Hello,my name is Abubakar and my full name is M Abubakar Raza"
print("Number of given value found in string :",demo.count("Abubakar"))


# endwith method check the given string is end with given value
# it will return True if string is end with provided value and respectively
print("Given string endswith :",demo.endswith("Raza"))
# you can also endswith with specific part of string
print("Given String endswith specific part :",demo.endswith("is",5,16))


# find method find first occurrence of given value in string and then return the index of first occurrence if it can't find it return -1

print("Find in String :", demo.find("is"))

# index method is similar to find but find return -1 if it can't find given value in string but index return error when it can't find given value

# For Now it is comment because it create error

# print("Index Method :",demo.index("da"))

# alnum return if given number is alphabet and number e.g A-Z a-z and 0-9
# if given string is alnum it return True otherwise False
test = "03march"
print("Is Given string is alphaNumeric",test.isalnum())

# isalpha is true when given string only contain alphabet (Lower or upper)
test2 = "march"
print("Is Given String is alpha :" , test2.isalpha())

# islower method check given string is in lower case if given string is in lower case it return true otherwise false
print("Given String is lower Case :",test2.islower())
  

# isupper method check given string is in upper case if given string is in upper case it return true otherwise false
print("Given String is upper Case :",test2.isupper())

# isprintable method return true if all the value in the given string is printable otherwise false

print("It is Printable",demo.isprintable())
test4 = "   Hello my name is Abubakar\n"
print("It is not Printable",test4.isprintable())

# isspace return true if given string contain whitespaces otherwise false
print("it contain ",test4.isspace())