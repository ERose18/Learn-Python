if 5 > 2:
    print("Five is Larger than two")
    #if 5 is larger than 2 then print the text within print

#############

my_name = "Evie"
print("Hello " + my_name + "!")
    #sets my_name to "Evie" and then prints "Hello Evie!" into the terminal

#############

print("Hello", end=" ")
print("World")
    #Each print by defauly will print onto a new line, by using end=" ", the next print will continue on the same line as the previous print
    
#############

#Naming Conventions!

#For naming in Python you can use both Uppercase and Lowercase naming for your variables such as Result and result.
#However, names are case sensitive and therefore if you had myname= "Evie", you cannot call it as Myname.. it must be "myname"
#You can have numbers within the names of your variables but never at the start. for example, result10 is good but 10result is bad.
#You are able to use an underscore anywhere in the name of the variable such as _result or result_
#Spaces cannot be in variable names so we must use snake_case. for example you can use "my_result" but not "my result".

#############

#Numbers!

print(10)  # A positive integer
print(-3000)  # A negative integer

num = 123456789  # Assigning an integer to a variable
print(num)
num = -16000  # Assigning a new integer
print(num)

#in Python, every negative number begins with a -

print(1.00000000005)  # A positive float
print(-85.6701)  # A negative float

float_num = 1.23456789
print(float_num)

#In Python, 5 is considered to be an integer while 5.0 is a float.

#template for making a complex number:
#complex(real, imaginary)
#Just like the print() statement is used to print values, complex() is used to create complex numbers.

print(complex(10, 20))  # Represents the complex number (10 + 20j)
print(complex(2.5, -18.2))  # Represents the complex number (2.5 - 18.2j)

complex_1 = complex(0, 2)
complex_2 = complex(2, 0)
print(complex_1)
print(complex_2)

#############

#Boolean!

#In Python we can just use True or False to represent a Boolean value

print(True)

f_bool = False
print(f_bool)

#############

#Strings!

print("Harry Potter!")  # Double quotation marks

got = 'Game of Thrones...'  # Single quotation marks
print(got)
print("$")  # Single character

empty = ""
print(empty)  # Just prints an empty line

multiple_lines = '''Triple quotes allows
multi-line string.'''
print(multiple_lines)

#The length of a string can be found using the len() function.

random_string = "I am Batman"  # 11 characters
print(len(random_string))

#every character is given a numerical index based on its position.
#A string in Python is indexed from 0 to n-1 where n is its length. This means that the index of the first character in a string is 0.

#Each character in a string can be accessed using its index. The index must be closed within square brackets, [], and appended to the string.

batman = "Bruce Wayne"

first = batman[0]  # Accessing the first character
print(first)

space = batman[5]  # Accessing the empty space in the string
print(space)

last = batman[len(batman) - 1]
print(last)

#We can also change our indexing convention by using negative indices.

batman = "Bruce Wayne"
print(batman[-1])  # Corresponds to batman[10]
print(batman[-5])  # Corresponds to batman[6]

#Once we assign a value to a string, we can’t update it later.

#assigning a new value to string variable doesn’t mean that you’ve changed the value. Let’s verify it with the id() method below.

str1 = "hello"
print(id(str1))

str1 = "bye"
print(id(str1))

#In Python 3.x, all strings are unicode. But, older versions of Python (Python 2.x) support only ASCII characters.
#To use unicode in Python 2.x, preceding the string with a u is must. For example:
#string = u"This is unicode"

#############

#The None Keyword!

#Python offers another data type called NoneType. It only has a single value, None.
# We can assign None to any variable, but we can not create other NoneType variables.

val = None
print(val) # prints "None" and returns None
print (type(val))

#None is not a default value for the variable that has not yet been assigned a value.
#None is not the same as False.
#None is not an empty string.
#None is not 0

#############

#String Slicing!

#Slicing is the process of obtaining a portion (substring) of a string by using its indices.

#Given a string, we can use the following template to slice it and obtain a substring:

    #string[start:end] 

        #start is the index from where we want the substring to start.
        #end is the index where we want our substring to end.

#The character at the end index in the string, will not be included in the substring obtained through this method.

my_string = "This is MY string!"
print(my_string[0:4]) # From the start till before the 4th index
print(my_string[1:7])
print(my_string[8:len(my_string)]) # From the 8th index till the end

#Python 3 also allows us to slice a string by defining a step through which we can skip characters in the string.
# The default step is 1, so we iterate through the string one character at a time.

#The step is defined after the end index:

    #string[start:end:step]
    
my_string = "This is MY string!"
print(my_string[0:7])  # A step of 1
print(my_string[0:7:2])  # A step of 2
print(my_string[0:7:5])  # A step of 5

#The output of print(my_string[0:7:5]) should be "Ti s"

#Strings can also be sliced to return a reversed substring. In this case, we would need to switch the order of the start and end indices.
#A negative step must also be provided:

my_string = "This is MY string!"
print(my_string[13:2:-1]) # Take 1 step back each time
print(my_string[17:0:-2]) # Take 2 steps back. The opposite of what happens in the slide above

#One thing to note is that specifying the start and end indices is optional.

#If start is not provided, the substring will have all the characters until the end index.

#If end is not provided, the substring will begin from the start index and go all the way to the end.

my_string = "This is MY string!"
print(my_string[:8])  # All the characters before 'M'
print(my_string[8:])  # All the characters starting from 'M'
print(my_string[:])  # The whole string
print(my_string[::-1])  # The whole string in reverse (step is -1)

#############

#String Formatting!

#String formatting means substituting values into a string. Following are some use cases of string formatting:

    #Inserting strings within a string
    #Inserting integers within a string
    #Inserting floats within a string


#Inserting Strings Within a String#

string1 = "I like %s" % "Python"
print(string1) # 'I like Python'

temp = "Educative"
string2 = "I like %s" % temp
print(string2) # 'I like Educative'

string3 = "I like %s and %s" % ("Python", temp)
print(string3)  # 'I like Python and Educative'

#The %s is the format specifier, which tells Python to insert the text here. Python will insert a string if:

    #We follow the string with a % and another string.
    #We follow the string with a % and another string type variable.
    #We can also insert multiple strings by putting multiple instances of %s inside our string


#Inserting Integers Within a String#

my_string = "%i + %i = %i" % (1,2,3)
print(my_string) # '1 + 2 = 3'

#The %i is the format specifier, which tells Python to insert the integers here.


#Inserting Floats Within a String#

string1 = "%f" % (1.11)
print(string1) # '1.110000'

string2 = "%.2f" % (1.11)
print(string2) # '1.11'

string3 = "%.2f" % (1.117)
print(string3) # '1.12'


#%f is used to substitute floats within a string. Note, string1 includes extra zeroes. 
# How about limiting 1.111.11 to two decimal places? We can use %.2f 

#If we pass a float that’s greater than two decimal places, then %.2f will round off the number (line 7).

