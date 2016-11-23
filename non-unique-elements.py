'''
You are given a non-empty list of integers (X). For this task, 
you should return a list consisting of only the non-unique elements 
in this list. To do so you will need to remove all unique elements 
(elements which are contained in a given list only once). 
When solving this task, do not change the order of the list. 
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and 
result will be [1, 3, 1, 3].

Input: A list of integers.
Output: The list of integers.

How it is used: This mission will help you to understand how 
to manipulate arrays, something that is the basis for solving 
more complex tasks. The concept can be easily generalized for 
real world tasks. 
For example: if you need to clarify statistics by removing 
low frequency elements (noise).
Precondition:
0 < len(data) < 1000
'''

def get_unique_keys(data):
	a_dict = get_hash(data)
	return [k for k, v in a_dict.items() if v == 1]

def get_hash(data):
	a_dict = {}
	for key in data:
		if key in a_dict:
			a_dict[key] += 1
		else:
			a_dict[key] = 1
	return a_dict

def remove_unique(data, unique_keys):
	data = data.copy()
	for key in unique_keys:
		indexes = [i for i,x in enumerate(data) if x == key]
		for index in indexes:
			del data[index]
	return data

def checkio_my_sln(data):
	data = data.copy()
	unique_keys = get_unique_keys(data)
	return remove_unique(data, unique_keys)

def checkio_online_sln(data):
	return [x for x in data if data.count(x) > 1]

l1 = [1, 2, 3, 1, 3]
l2 = [1, 2, 3, 4, 5]
l3 = [5, 5, 5, 5, 5]
l4 = [10, 9, 10, 10, 9, 8]
l5 = ['a', 'b', 'b', 'c', 'c', 'd', 'd', 'd']

lall = [l1, l2, l3, l4, l5]

for l in lall:
	print("{} {}".format(l,checkio_my_sln(l)))

print("\n")

for l in lall:
	print("{} {}".format(l,checkio_online_sln(l)))
