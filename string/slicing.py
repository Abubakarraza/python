name = 'Abubakar Raza'
# you can get the length of string using len() function
# it print the length of string 
print(len(name))
# you can slice string 
# I want to print Abubakar not Raza
# it include 0 index value but not last index value
print(name[0:8])
# it also print Abubakar because python default first value is 0
print(name[:8])
# you can also access with -ve index value 
# but in negative index start with -1 not 0
# in that case we get Raza 
print(name[-4:])
# in that case we get Raz
print(name[-4:-1])
