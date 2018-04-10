'''a little piece of py
Author: Frank J. Genova
Created: 2018-04-09
'''

def do_something(what):
	print(f'I will do {what} you want with in-line interpolation')
	print('They say {} is better than {}'.format('Python', 'MUMPS')
	return True
	
def main():
	do_what = input('What shall I do')
	this_what = do_something(do_what)
	print(this_what)
	return True
	
if __name__ == "__main__":
	# execute only if run as script
	main()
	
	# '__main__' is the name of the scope in which top-level code executes. 
	
	# A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt.
	
	# A module can discover whether or not it is running in the main scope by checking its own __name__, 
	# which allows a common idiom for conditionally executing code in a module when it is run as a script 
	# or with python -m but not when it is imported:
	
	# For a package, the same effect can be achieved by including a __main__.py module, 
	# the contents of which will be executed when the module is run with -m.
