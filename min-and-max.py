''' 
In this mission you should write you own py3 implementation (but
you can use py2 for this) of the built-in functions min and max. Some
builtin functions are closed here: import, eval, exec, globals. Don't
forget you should implement two functions in your code.

max(iterable, *[, key]) or min(iterable, *[, key]) max(arg1, arg2,
*args[, key]) or min(arg1, arg2, *args[, key])

Return the largest (smallest) item in an iterable or the
largest(smallest) of two or more arguments.

If one positional argument is provided, it should be an iterable. The
largest (smallest) item in the iterable is returned. If two or more
positional arguments are provided, the largest (smallest) of the
positional arguments is returned.

The optional keyword-only key argument specifies a function of one
argument that is used to extract a comparison key from each list
element (for example, key=str.lower).

If multiple items are maximal (minimal), the function returns the
first one encountered.

-- Python Documentation (Built-in Functions)

Input: One positional argument as an iterable or two or more
positional arguments. Optional keyword argument as a function.

Output: The largest item for the "max" function and the smallest for
the "min" function.

Example:

max(3, 2) == 3
min(3, 2) == 2
max([1, 2, 0, 3, 4]) == 4
min("hello") == "e"
max(2.2, 5.6, 5.9, key=int) == 5.6
min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
    

How it is used: This task will help you understand how some of the
built-in functions work on a more precise level.

Precondition: All test cases are correct and functions don't have to
raise exceptions.
'''

import unittest

def comp(args, kwargs, comp_fn):
	if len(args) == 1:
		args = [arg for arg in args[0]]
	f = kwargs.get("key", lambda x: x)
	m, mf = args[0], f(args[0])
	for arg in args:
		if comp_fn(f(arg), mf):
			m, mf = arg, f(arg)
	return m

def max(*args, **kwargs):
	return comp(args, kwargs, lambda x,y: x > y)

def min(*args, **kwargs):
	return comp(args, kwargs, lambda x,y: x < y)


class Test(unittest.TestCase):
	def test_max(self):
		assert max(3,2) == 3
		assert max(1,2,0,3,4) == 4
		assert max([1,2,0,3,4]) == 4
		assert max([1,2,0,3,4],[5,6]) == [5, 6]		
		assert max([[1,2,0,3,4],[5,6]]) == [5, 6]
		assert max("h","e","l","l","o") == "o"
		assert max("hello") == "o"
		assert max(2.2, 5.6, 5.9, key=int) == 5.6
		assert max([1, 2], [3, 4], [9, 0], key=lambda x: x[1]) == [3, 4]
		assert max([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [3, 4]


	def test_min(self):
		assert min(3,2) == 2
		assert min(1,2,0,3,4) == 0
		assert min([1,2,0,3,4]) == 0
		assert min([1,2,0,3,4],[5,6]) == [1,2,0,3,4]
		assert min([[1,2,0,3,4],[5,6]]) == [1,2,0,3,4]
		assert min("h","e","l","l","o") == "e"
		assert min("hello") == "e"
		assert min(2.2, 5.6, 5.9, key=int) == 2.2
		assert min([1, 2], [3, 4], [9, 0], key=lambda x: x[1]) == [9, 0]
		assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]


if __name__ == '__main__':
	unittest.main()
