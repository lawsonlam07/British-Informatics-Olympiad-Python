i, f = 0, float(input("Decimal: "))

while True:
  i += 1
  fraction = i/f
  if fraction.is_integer():
    print(str(i) + "/" + str(int(i/f)))
    break
  # Because python is garbage at maths and 401/0.2005 gives 1999.999999... rather than 2000, which breaks the code.
  elif str(fraction).split(".")[1][0:12] == "9" * 12: # Checks if the decimal is reoccuring.
    print(str(i) + "/" + str(int(i/f) + 1))
    break
