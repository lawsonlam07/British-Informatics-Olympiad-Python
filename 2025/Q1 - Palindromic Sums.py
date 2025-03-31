from itertools import combinations_with_replacement as comb


target = int(input("Enter an integer: "))
palindromes = list(filter(lambda x: str(x) == str(x)[::-1], range(1, target + 1)))

c1 = list(filter(lambda x: x == target, palindromes))

if c1:
   print(c1[0])
   exit()

c2 = list(filter(lambda x: sum(x) == target, comb(palindromes, 2)))

if c2:
   smallest = min(list(map(lambda x: min(x), c2)))
   c2 = list(filter(lambda x: min(x) == smallest, c2))
   print(c2[0])
   exit()

c3 = list(filter(lambda x: sum(x) == target, comb(palindromes, 3)))

if c3:
   smallest = min(list(map(lambda x: min(x), c3)))
   c3 = list(filter(lambda x: min(x) == smallest, c3))
   largest = max(list(map(lambda x: max(x), c3)))
   c3 = list(filter(lambda x: max(x) == largest, c3))
   print(c3[0])
   exit()
