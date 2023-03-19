x = int(input("Please Enter any Number:"))
match x:
    case 0:
        print('Number is zero')
    case 10:
        print("Number is 10")
    case _ if x > 10 and x <= 20:
        # you can also apply condition just like 👆
        print("Number is in between 11 - 20")
    case _:
         # _ is used for default case just like else case
        print(x)    
    

