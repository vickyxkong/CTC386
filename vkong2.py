#Vicky Kong
#Lab 2

#function
def bitcoverter(b1,b2,b3,b4,b5,b6):
    num1=b1*2**0
    num2=b2*2**1
    num3=b3*2**2
    num4=b4*2**3
    num5=b5*2**4
    num6=b6*2**5
    num=num1+num2+num3+num4+num5+num6
    return num

#main

bit1=int(input("Enter the first bit:"))
bit2=int(input("Enter the second bit:"))
bit3=int(input("Enter the third bit:"))
bit4=int(input("Enter the fourth bit:"))
bit5=int(input("Enter the fifth bit:"))
bit6=int(input("Enter the sixth bit:"))

total=bitcoverter(bit1,bit2,bit3,bit4,bit5,bit6)
print("The number is",total)
