import random
import string


def generateRandomString():
    return ''.join(random.choices(string.ascii_lowercase,k=5))


def codeString(value):
    if(len(value)>3):
        newString=value[1:len(value)]
        newString+=value[0]
        start = generateRandomString()
        end = generateRandomString()
        newString=start+newString+end
        return newString
    else:
        print("String must be greater than 3")
def decode(value):
    value=value[5:-5]
    newString=value[0:len(value)-1]
    newString=value[len(value)-1]+newString
    return newString

value=str(input("Enter any string to code:"))
codedString=codeString(value)
print("CodedString:",codedString)

isDecode=input("Do you want to decode your String:")

if isDecode == "yes" or isDecode=="y":
    print("Decoded String:",decode(codedString))