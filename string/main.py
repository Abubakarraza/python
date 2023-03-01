# in python you can print any text using singleQuote('') and double quote("")
name = 'Abubakar'
brother = 'Abdullah'
print("Hello my name is ",name)
print("MY Bro name is ",brother)
# also you can print multiple line using triple quote or sequence Character
about =''' Hello my name 
is abubakar and 
i am new in python programming'''
print(about)
# escape sequence character n\
exp=" i have 1+ year of experience in java script n\
and now i want to learn python"
# In python string is like an array of character and you can access part of string by using index
print(name[0])
# Now it print A because first character of name is A
# There is way to print all string with separate index using for loop
for character in exp:
    print(character)