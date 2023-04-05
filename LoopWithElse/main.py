# Else in Loop

# As you have learned before , the else clause is used along with the if statement.

# python allows the else keyword to be used with the for and while loops too. The else block appear after the body of the loop. The statement in the else block will be executed after all iteration are completed. The program exist the loop only after the else block is executed

# Example:for loop

for i in range(5):
    print(i)
else:
    print("else block in loop")   

# Example : while loop

num=10

while num > 5:
    print(num)
    num-=1
else:
    print("while loop else block")


# Note : if we use break keyword in loop than else is not run 

for i in range(6):
    if(i==4):
        break
    print(i)
else:
    print("else with break keyword")        
# because break keyword end the loop   