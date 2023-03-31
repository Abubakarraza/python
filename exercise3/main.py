# Exercise #3
# Kon bane ga Crorepati program
name = input("Your name:")
question=["Translates the source code into machine language",'The step by step procedure for solving a problem','communication between user and the computer is','The step by step procedure for solving a problem','The language processor translates the program into object code as a whole']
options=[['operating system','programming language','language processor','all of these'],['programming','algorithm','planing','flowchart'],["programming language",'software','syntax','english language'],['programming','algorithm','planing','flowchart'],['linker','debugger','compiler','interpreter']]
answers=['language processor','algorithm','programming language','algorithm','compiler']
prize=0
for index, item in enumerate(question):
    print(f"Question:{index + 1}",item)
    for i , y in enumerate(options[index]):
        print(i,":",y)
    userAnswer = str(input("Your Answer:"))
    if userAnswer == answers[index]:
        prize+=1000       
if prize > 0:
  print(f"Hey,{name} you won {prize} prize money ✨🎉")
else:
    print(f"{name} you did not win any prize😢")  