string = input("Enter a string:")
def count_code(str):
  count = 0
  for i in range(len(str) - 3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count

print(count_code(string))
