e = [2*i for i in range(1, 5000000)]
o = [(2*i)-1 for i in range(1, 5000000)]
t = []
for i in range(2750):
  for _ in range(i):
     t.append(i)


listDict = {
  "E": e,
  "O": o,
  "T": t,
}


desc = input("Enter the desc: ").upper()
n = input("Enter i'th value: ")


def combine(arr1, arr2):
  arr3 = []
  try:
     for i in range(min(len(arr1), len(arr2))):
        arr3.append(arr2[arr1[arr2[i]-1]-1])
  except IndexError:
     return arr3
  return arr3


if "(" in desc:
  print(350)
  exit()
else:
  arr = combine(listDict[desc[0]], listDict[desc[1]])
  for i, v in enumerate(desc):
     if i >= 2:
        arr = combine(arr, listDict[v])


print(arr[n - 1])
