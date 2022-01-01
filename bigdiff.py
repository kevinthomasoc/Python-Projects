text = input("Enter a list of numbers (separated by spaces): ")
text = text.split()
numlist = []
for i in text:
    newint = int(i)
    numlist.append(newint)

def big_diff(nums):
  maxnum = 0
  minnum = 1000000
  for i in range(len(nums)):
    if nums[i] > maxnum:
      maxnum = (nums[i])
    if nums[i] < minnum:
      minnum = (nums[i])
  return maxnum - minnum

print(big_diff(numlist))
