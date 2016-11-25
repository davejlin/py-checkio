''' 
You are given an array of integers. You should find the sum of the
elements with even indexes (0th, 2nd, 4th...) then multiply this
summed number and the final element of the array together. Don't
forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.

Example:

checkio([0, 1, 2, 3, 4, 5]) == 30 
checkio([1, 3, 5]) == 30
checkio([6]) == 36 
checkio([]) == 0 1 2 3 4 

How it is used: Indexes
and slices are important elements of coding in python and other
languages. This will come in handy down the road!

Precondition: 0 ≤ len(array) ≤ 20 
all(isinstance(x, int) for x in
array) all(-100 < x < 100 for x in array)
'''
from functools import reduce
def checkio(array):
	try:
		s = reduce(lambda x,y: x+y, [v for n,v in enumerate(array) if n%2 == 0])
		return s*array[-1]
	except:
		return 0

inputs = [
	[0, 1, 2, 3, 4, 5],
	[1, 3, 5],
	[6],
	[]
]

for inp in inputs:
	print(checkio(inp))