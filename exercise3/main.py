# Exercise #3
# Kon bane ga Crorepati program
name = input("Your name:")
question=["Translates the source code into machine language",'The step by step procedure for solving a problem','communication between user and the computer is','The step by step procedure for solving a problem','The language processor translates the program into object code as a whole']
options=[['operating system','programming language','language processor','all of these'],['programming','algorithm','planing','flowchart'],["programming language",'software','syntax','english language'],['programming','algorithm','planing','flowchart'],['linker','debugger','compiler','interpreter']]
answers=['language processor','algorithm','programming language','algorithm','compiler']
prize = 0
for index, item in enumerate(question):
    print(f"Question:{index + 1}",item)
    for i , y in enumerate(options[index]):
        print(i,":",y)
    userAnswer = int(input("Enter your answer b/w 0-3:"))
    if userAnswer < 0 or userAnswer > 3:
        print("Invalid Answer")
        continue

    if options[index][userAnswer] == answers[index]:
        prize+=1000       
if prize > 0:
  print(f"Hey,{name} you won {prize} prize money ✨🎉")
else:
    print(f"{name} you did not win any prize😢")  