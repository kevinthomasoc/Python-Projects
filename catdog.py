userinput = input("Enter a string:")
def cat_dog(str):
  countcat = 0
  countdog = 0
  for i in range(len(str)):
    if str[i:i+3] == 'cat':
      countcat += 1
    if str[i:i+3] == 'dog':
      countdog += 1
  if countdog == countcat:
    return True
  else:
    return False

print(cat_dog(userinput))
