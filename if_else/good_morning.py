import time
getHour =int( time.strftime('%H '))
if(getHour >= 5 and getHour <  12):
    print("Good Morning")
elif(getHour >=12 and getHour < 18):
    print("Good Afternoon")
else: 
    print("Good Evening")