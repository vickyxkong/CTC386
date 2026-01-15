#Vicky Kong
#GitHub test comment

name=str(input("Enter your name:"))

print("Menu")
print("-----------------")
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("-----------------")

def calculateCelsius(F):
    C=(F-32)*(5/9)
    return C

print("Hi",name)
option=input("Enter a number to choose an option:")
x=int(option)

if(x==1):
    print("Not all math jokes are bad. Just sum.")

if(x==2):
    y=15
    for i in range(y):
        print(name)

if(x==3):
    z=int(input("Enter a number."))
    for i in range(z):
        print("You're really the only one who needs to acknowledge your effort.")

if(x==4):
    v=int(input("Enter a number between the range of 0 and 100."))
    while(v!=12):
        while (v<0)or(v>100):
            print("Your number is not in the range.")
            v=int(input("Enter a number between the range of 0 and 100."))
        if(v<12):
            print("Too low! Try again.")
        if(v>12):
            print("Too high! Try again.")
        v=int(input("Enter a number between the range of 0 and 100."))
    if(v==12):
          print("You have won! You are super smart!")

if(x==5):
    F=int(input("Enter the current temperature in Fahrenheit:"))
    Celsius=calculateCelsius(F)
    print("The current tenperature is",Celsius,"degree Celsius.")
