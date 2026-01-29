#Vicky Kong
#Final Question 4

#function

def HNY(n):
    for i in range(n):
        print("HAPPY NEW YEAR!")

#main

n=int(input("Enter a number between 1 and 10:"))
while(n<1)or(n>10):
    print("Your number is not within 1 and 10.")
    n=int(input("Enter a number between 1 and 10:"))
if(n>=1)and(n<=10):
    HNY(n)

