def rotate(l, n):
    return l[n:] + l[:n]

def Search(Nums, target):
  # Check:
  OK=1
  if not (1<=len(Nums)<=5000): OK=0
  for k in Nums:
    if not ( -10^4 <= k <=10^4):
      Ok=0

  if OK:
    for k in range(len(Nums)):
      if(Nums[k]==target): 
        return k
    return -1
  else:
    return None

target=0
Nums=[4,5,6,7,0,1,2]
print(Search(Nums, target))

Nums = [4,5,6,7,0,1,2]
target = 3 
print(Search(Nums, target))

Nums = [1]
target = 0
print(Search(Nums, target))
# expect: 4,-1,-1
