#Vicky Kong
#Final Question 1

print("Menu")
print("---------------")
print("Option 1")
print("Option 2")
print("Option 3")
print("---------------")

option=input("Enter a number to choose an option:")
x=int(option)

if(x==1):
    name=str(input("Enter your name:"))
    print(name,",do you know what happens when a frog's car breaks down?")
    print("It gets toad! HAHAHA")

elif(x==2):
    for i in range(20):
        print("hot pot")

elif(x==3):
    y=1
    while(y!=0):
        y=int(input("Enter a number:"))
        if(y!=0):
            print("You did not gues the number. Try again!")
    else:
        print("You have guess the number is 0!")
