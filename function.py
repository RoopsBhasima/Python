
#Functions
#FirstFunction

def xyz():
	print('Printing from a function')
xyz()

#calling function
print(xyz())

#First function with para

def para_func(str):
	return str
print(para_func('a'))

#second function with two parameters
def para_func2(first_name,last_name):
	print(first_name,last_name)
para_func2('rupesh','bhasima')

def default_parameter(name='Samriddhi'):
	print('Hello' + name)
default_parameter()

fruits=['Mango','Banana','Cherry']
def loop(fruits):
	for fruit in fruits:
		print(fruit)
loop(fruits)
