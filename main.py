import random
max = input("What is the highest number you want to guess up to? ")
#Check if max is a number
if max.isdigit():
    max = int(max)
else:
    print("You did not enter a number greater than 0, please restart the program.")

randInt = random.randint(0,max)

guess = input("Guess a number: ")

while guess != randInt:
    if int(guess) == randInt:
        break
    if int(guess) > randInt:
        print("The number is lower!")
    if int(guess) < randInt:
        print("The number is higher!")
    guess = input("Guess a number: ")


print("You guess it! The number is " + str(randInt) + "!")
quit()

