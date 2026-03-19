#Midterm Question 13
#Vicky Kong

#Write a Python program, using the class server, that asks a user to enter a number between 1 and 10. If the user guesses a number you choose, display that result to the user. If the user does not guess your number, display that result.

g=int(input("Guess a number between 1 and 10:"))

if (g==8):
    print("You have guessed the right number!")

elif (g!=8):
    if(g>0 and g<11):
        print("You have guessed the wrong number!")
    elif(g<1 or g>10):
        print("You guessed a number out of the range.")

