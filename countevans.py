text = input("Enter a list of numbers (separated by spaces):")
text = text.split()
newnums = []
for i in text:
    integer = int(i)
    newnums.append(integer)
print(newnums)
    
def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count

print(count_evens(newnums))
