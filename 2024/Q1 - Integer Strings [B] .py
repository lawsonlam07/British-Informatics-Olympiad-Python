# If you're not bruteforcing this question, the logic behind it isn't very intuitive, hence the comments.

intervals = [0] + [int(str(i) + "8"*i + "9") for i in range(100)]
# Makes an array of all the characters where the number of digits changes.
# E.g. There are 9 one digit numbers (9 chars total)
# There are 90 two digit numbers (9 + 180 = 189 chars total) [180 = 90 * 2]
# There are 900 three... (189 + 2700 = 2889 chars total) [2700 = 900 * 3]
# And so on.
# Therefore, the array goes [0, 9, 189, 2889, 3889, 4889...]

# Here's what this array tells us.
# One digit numbers have an index value of between 0 and 9,
# Two digit numbers have an index value of between 9 and 189...

start, index = [int(v) for v in input("Enter n and i: ").split(" ")]
startDigits = len(str(start))

index += intervals[startDigits-1] + startDigits*(start - int("1" + "0"*(startDigits - 1)))
# Instead of rewriting the string, I just decided to shift the index value to the appropriate spot.

digits = intervals.index(next(v for v in intervals if v >= index))
# We check how many digits the number in the indexed position would have.
d, m = divmod(index - intervals[digits - 1] - 1, digits)
# We then work out the number at that position, and the index of the exact character we want.
# If it helps you understand, use: print(d + 10**(digits-1), m)
# It returns the full number that the index references, and the specific character in that number.

print(str(d + 10**(digits-1))[m])

"""
Difficulty: B
While bruteforce generating the string is the easiest method (lowering the difficulty to E),
you lose out on marks as the algorithm will run over the 1s time limit given.

It could be as simple as this:

start, index = [int(v) for v in input("Enter n and i: ").split(" ")]
string = "".join(str(i) for i in range(start, start+index))
print(string[index-1])

Instead, you can do a lot of maths to work out the exact number that would be in that spot,
and the character index that is needed to be returned. My methods are explained in the comments.
"""
