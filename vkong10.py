#Vicky Kong
#lab 10

#functions
def calculateCelsius(F):
    C=(F-32)*(5/9)
    return C

def plvmember():
    print("Nam Yejun: Leader and main vocalist of the group. Color representation: Blue")
    print("Han Noah: Oldest and main vocalist of the group. Color representation: Purple")
    print("Chae Bamby: Main dancer and vocalist of the group. Color representation: Pink")
    print("Do Eunho: Main rapper and vovalist of the group. Color representation: Red")
    print("Yu Hamin: Main dancer, lead rapper, and youngest of the group. Color representation: Green")

#main
name=str(input("Enter your name:"))

print("Menu")
print("-----------------")
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("Option 6")
print("-----------------")


print("Hi",name)
option=input("Enter a number to choose an option:")
x=int(option)

if(x==1):
    print("Not all math jokes are bad. Just sum.")

elif(x==2):
    y=15
    for i in range(y):
        print(name)

elif(x==3):
    z=int(input("Enter a number."))
    for i in range(z):
        print("You're really the only one who needs to acknowledge your effort.")

elif(x==4):
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

elif(x==5):
    F=int(input("Enter the current temperature in Fahrenheit:"))
    Celsius=calculateCelsius(F)
    print("The current tenperature is",Celsius,"degree Celsius.")

elif(x==6):
    print("Learn about PLAVE,a virtual K-Pop group!")
    print("1. Members")
    print("2. Debut Date")
    print("3. Learn the fanchant!")
    p=int(input("Choose a number:"))
    if(p==1):
        plvmember()
    elif(p==2):
        print("PLAVE debut on March 12th, 2023.")
    elif(p==3):
        for i in range(5):
            print("Nam Yejun! Han Noah! Chae Bamby! Do Eunho! Yu Hamin! PLAVE!")

