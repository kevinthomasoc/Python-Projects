print("Welcome to my Capitals quiz game!")

playing = input("Do you want to take the quiz? (Y/N) ")

#Check to see if the user wants to play, if not, quit.
if (playing != "y"):
    print("Quitting!")
    quit()

numCorrect = 0

#First Question
answer = input("What is the capital of California? ")
if answer.lower() == "sacramento":
    print("Correct!")
    numCorrect += 1
else:
    print("Incorrect!")

#Second Question
answer = input("What is the capital of the United States? ")
if answer.lower() == "washington d.c.":
    print("Correct!")
    numCorrect += 1
else:
    print("Incorrect!")

#Third Question
answer = input("What is the capital of Canada? ")
if answer.lower() == "ottawa":
    print("Correct!")
    numCorrect += 1
else:
    print("Incorrect!")

print("You got " + str(numCorrect) + " questions correct!")
print("You got " + str((numCorrect/3) * 100) + "% correct!")