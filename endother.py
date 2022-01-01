y = input("Enter first string:")
z = input("Enter second string:")
def end_other(a, b):
    alength = len(a)
    blength = len(b)
    bstring = b[-alength:]
    astring = a[-blength:]
    if a.lower() == bstring.lower():
        return True
    elif b.lower() == astring.lower():
        return True
    else:
      return False
print(end_other(y,z))
