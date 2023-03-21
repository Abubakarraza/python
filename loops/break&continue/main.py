# break
# The break statement enable a programme to skip over a part of the code. A break statement terminate the very loop it lies within
for i in range(12):
    if(i > 10):
        break
    print("10 X",i,"=",5*i)   



# continue
# The continue statement skip the rest of the loop statement and cause the next iteration to occur

for i in range(12):
    if(i == 10):
        print("skip iteration")
        continue
    print("10 X",i,"=",5*i) 


# do while loop in py
i = 0
while True:
    print(i)
    i+=1
    if(i % 100 == 0):
        break