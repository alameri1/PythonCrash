#a string in python is surronded by either a single or double quotation marks. lets look at 
#string formatting and some usufull methods

name = "Abdulla"
age = 25

#concatenate
#String formmating 

print('hello, my name is ' + name + 'and I am ' + str(age))
#or
#argumantes by position
print( "my name is {name} and I am {age}".format(name=name, age=age))
#f-string(only for py 3.6+)
print(f'Hello, my name is {name} and i am {age}')
#string methods 
s = 'hello world'

#Capitlize string
print(s.capitalize())
#make all upper case
print(s.upper())
#make all lower case
print(s.lower())
#swap case!
print(s.swapcase())
#get length
# can be used for any data type
print(len(s))
#Replace
print(s.replace('world','everyone'))

#count
sub = 'h'
print(s.count(sub))

#starts with return  bool 
print(s.startswith("hello"))
#Ends with return bool
print(s.endswith('d'))
#split into a list/ a type of array
print(s.split())
#find position, returns nuber
print(s.find('r'))
#is all alpabatic? returns bool
print(s.isalpha())
#is all alphanemeric? returns bool
print(s.isalnum())
#is all numeric? returns bool
print(s.isnumeric())
