#function definition
userinput = input("Enter a string:")
def xyz_there(str):
    #Checks if xyz is in the string
    if ("xyz" in str) == True:
        #Checks if period is in string
        if ("." in str) == True:
            #For each letter in the string, I convert it to integers so I can slice the string.
            for i in range(len(str)):
                #If I index string starting from i and ending at i+3 and I find xyz, and the character before i is not a period, return True
                if str[i:i+3] == "xyz" and str[i-1] != ".":
                    return True
                #If I find xyz and the character before the x is a period, continue back to the loop. If I reach an index where i+3 is greater than the length of the string, I return False because I know xyz cannot exist there. 
                elif str[i:i+3] == "xyz" and str[i-1] == ".":
                  continue
                if (i+3) > (len(str)):
                  return False
        #If period is not in string, find xyz and return True
        elif ("." in str) == False:
            for i in range(len(str)):
                if str[i:i+3] == "xyz":
                    return True
    #If xyz is not in string, return False
    else:
        return False

print(xyz_there(userinput))
