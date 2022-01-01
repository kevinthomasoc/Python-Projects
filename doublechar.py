string = input("Enter a string:")
def double_char(str):
  string = ""
  for char in str:
    string = string + char*2
  return string
print(double_char(string))
