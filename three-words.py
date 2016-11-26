''' 
Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces
(one space). The words contains only letters. You should check if the
string contains three words in succession. For example, the string
"start 5 one two three 7 end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.

Example:

checkio("Hello World hello") == True 
checkio("He is 123 man") == False
checkio("1 2 3 4") == False 
checkio("bla bla bla bla") == True
checkio("Hi") == False 

How it is used: This teaches you how
to work with strings and introduces some useful functions.

Precondition: The input contains words and/or numbers. There are no
mixed words (letters and digits combined). 0 < len(words) < 100 
'''
import re
def checkio(words):
	return True if re.findall(r'((?:\b[^\d\W]+\b\s*){3})',words) else False

inputs = [
	"Hello World hello",
	"He is 123 man",
	"1 2 3 4",
	"bla bla bla bla",
	"Hi",
	"one two 2.5 three four 4.5 five six seven eight"
]

for inp in inputs:
	print(checkio(inp))