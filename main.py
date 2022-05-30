def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            print(line.rstrip())

def add():
    service = input("Enter what service the account is made for (E.g. Spotify): ")
    username = input("Enter the account username: ")
    password = input("Enter the account password: ")

    with open("passwords.txt", "a") as file:
        file.write("Service: " + service + " Username: " + username + " Password: " + password + "\n")


def delete(servicename):
    with open("passwords.txt", "r") as file:
        lines = file.readlines()
    with open("passwords.txt", "w") as file:
        found = False
        for line in lines:
            if (servicename in (line.strip()).lower()) == False:
                file.write(line)
            else:
                found = True
        if found == True:
            return("Your account information for " + servicename + " has been deleted.")
        else:
            return("Your account information for " + servicename + " could not be found.")


masterPwd = input("What is the master password?")




while True:
    mode = input("Would you like to add a password, or view existing passwords (view, add, delete)?")
    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()
    elif mode.lower() == "delete":
        servicename = input("Enter the name of the service of the account you want deleted: ")
        servicename = servicename.lower()
        print(delete(servicename))
    else:
        print("Invalid Input.")
        continue