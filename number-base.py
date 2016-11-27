''' 
Do you remember the radix and Numeral systems from math class?
Let's practice with it.

You are given a positive number as a string along with the radix for
it. Your function should convert it into decimal form. The radix is
less than 37 and greater than 1. The task uses digits and the letters
A-Z for the strings.

Watch out for cases when the number cannot be converted. For example:
"1A" cannot be converted with radix 9. For these cases your function
should return -1.

Input: Two arguments. A number as string and a radix as an integer.

Output: The converted number as an integer.

Example:

checkio("AF", 16) == 175
checkio("101", 2) == 5
checkio("101", 5) == 26
checkio("Z", 36) == 35
checkio("AB", 10) == -1
    
How it is used: Here you will learn how to work with the various
numeral systems and handle exceptions.

Precondition:

re.match("\A[A-Z0-9]\Z", str_number)
0 < len(str_number) ≤ 10
2 ≤ radix ≤ 36 
'''

MAP = {
	'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
	'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,
	'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,
	'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35
}

def checkio(str_number, radix):
	digits = list(map(lambda x: MAP[x], list(str_number)))
	if max(digits) >= radix: return -1
	return sum([digit*radix**i for i, digit in enumerate(reversed(digits))])

def checkio_online_sln(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1

inputs = [
	("1567", 10),
	("AF", 16),
	("101", 2),
	("101", 5),
	("Z", 36),
	("AB", 10),
	("DEADBEEF", 16)
]

outputs = map(lambda x: checkio_online_sln(x[0],x[1]), inputs)
print(list(outputs))