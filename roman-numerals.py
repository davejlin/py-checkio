'''
Roman numerals come from the ancient Roman numbering system. 
They are based on specific letters of the alphabet which are combined to signify 
the sum (or, in some cases, the difference) of their values. 
The first ten Roman numerals are:
I, II, III, IV, V, VI, VII, VIII, IX, and X.
The Roman numeral system is decimal based but not directly positional and 
does not include a zero. Roman numerals are based on combinations of these seven symbols:
Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)

More additional information about roman numerals can be found on the Wikipedia article.
For this task, you should return a roman numeral using the specified integer value 
ranging from 1 to 3999.

Input: A number as an integer.
Output: The Roman numeral as a string.

How it is used: This is an educational task that allows you to explore different 
numbering systems. Since roman numerals are often used in the typography, 
it can alternatively be used for text generation. The year of construction on 
building faces and cornerstones is most often written by Roman numerals. 
These numerals have many other uses in the modern world and you read about it here... 
Or maybe you will have a customer from Ancient Rome ;-)

Precondition: 0 < number < 4000
'''

def compose(value, sym_1, sym_5, sym_10):
	s = ""
	if value == 9:
		s += sym_1 + sym_10
	elif value > 4:
		s += sym_5
		for _ in range(value-5):
			s += sym_1
	elif value < 4:
		for _ in range(value):
			s += sym_1
	else:
		s += sym_1 + sym_5
	return s


def checkio_my_ans(data):
	thousands, remainder = divmod(data, 1000)
	hundreds, remainder = divmod(remainder, 100)
	tens, ones = divmod(remainder, 10)

	s  = compose(thousands, "M", "", "")
	s += compose(hundreds, "C", "D", "M")
	s += compose(tens, "X", "L", "C")
	s += compose(ones, "I", "V", "X")
	
	return s

def checkio_online_ans(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result


numbers = [1, 4, 6, 14, 49, 76, 499, 528, 999, 1001, 1949, 2492, 3888]

for number in numbers:
	print("{} {}".format(str(number), checkio_my_ans(number)))

for number in numbers:
	print("{} {}".format(str(number), checkio_online_ans(number)))
