fhand = open("taylorswift.txt")
listt = []
allwords = []
unique = []
#Iterate through the textfile and make lists of each of the lines and attatch it to an empty list. 
for line in fhand:
    listt.append(line.split())
#Append each word onto an empty list called wordlist. Now that list only has words in it.     
for list in listt:
    for word in list:
        allwords.append(word)
#Create a list of unique words
for word in allwords:
    if (word not in unique) == True:
        unique.append(word)
#Checks for how many times a word occurs 
for word in unique:
    count = 0
    for secondword in allwords:
        if word.lower() == secondword.lower():
            count += 1
    print(word, count)




