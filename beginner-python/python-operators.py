#############

#Operators!

#Operators are represented by characters or special keywords.

#In general, Python’s operators follow the in-fix or prefix notations.

#In-fix operators appear between two operands (values on which the operator acts) and hence, are usually known as binary operators

#A prefix operator usually works on one operand and appears before it. Hence, prefix operators are known as unary operators

#The 5 main operator types in Python are:
    #arithmetic operators
    #comparison operators
    #assignment operators
    #logical operators
    #bitwise operators

#############

#Arithmetic Operators#

# Operator 	         Purpose 	        Notation

#  ()              	 Parentheses 	    Encapsulates the Precedent Operation

#  ** 	             Exponent 	        In-fix

#  %, *, /, // 	     Modulo,
#                    Multiplication,    In-fix
#                    Division, 
#                    Floor Division  	
                    
#  +, - 	         Addition, 
#                    Subtraction 	    In-fix


#Addition#

print(10 + 5)

float1 = 13.65
float2 = 3.40
print(float1 + float2)

num = 20
flt = 10.5
print(num + flt)

#Subtraction#

print(10 - 5)

float1 = -18.678
float2 = 3.55
print(float1 - float2)

num = 20
flt = 10.5
print(num - flt)

#Multiplication

print(40 * 10)

float1 = 5.5
float2 = 4.5
print(float1 * float2)

print(10.2 * 3)

#Division#

print(40 / 10)

float1 = 5.5
float2 = 4.5
print(float1 / float2)
print(12.4 / 2)

#Floor Division#

print(43 // 10)

float1 = 5.5
float2 = 4.5
print(5.5 // 4.5)
print(12.4 // 2)

#Modulo#

print(10 % 2)

twenty_eight = 28
print(twenty_eight % 10)

print(-28 % 10)  # The remainder is positive if the right-hand operand is positive
print(28 % -10)  # The remainder is negative if the right-hand operand is negative
print(34.4 % 2.5)  # The remainder can be a float

#Precedence#

# Different precedence
print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction

# Same precedence
print(3 * 20 / 5)  # Multiplication computed first, followed by division
print(3 / 20 * 5)  # Division computed first, followed by multiplication

#Parentheses#

print((10 - 3) * 2)  # Subtraction occurs first
print((18 + 2) / (10 % 8))


#############

#Comparison Operators#

# Operator 	    Purpose             	Notation
# > 	      Greater Than 	             In-fix
# < 	       Less Than 	             In-fix
# >= 	      Greater Than
#              or Equal To  	         In-fix
# <= 	      Less Than 
#              or Equal To  	         In-fix
# == 	        Equal To 	             In-fix
# != 	    Not Equal To 	             In-fix
# is 	Equal To (Identity) 	         In-fix
# is not 	Not Equal To (Identity) 	 In-fix


#Comparisons#

#The result of a comparison is always a bool.
#The == and != operators compare the values of both operands.
# However, the identity operators, is and is not, check whether the two operands are the exact same object.

num1 = 5
num2 = 10
num3 = 10
list1 = [6,7,8]
list2 = [6,7,8]

print(num2 > num1)  # 10 is greater than 5
print(num1 > num2)  # 5 is not greater than 10

print(num2 == num3)  # Both have the same value
print(num3 != num1)  # Both have different values

print(3 + 10 == 5 + 5)  # Both are not equal
print(3 <= 2)  # 3 is not less than or equal to 2

print(num2 is not num3)  # Both have the same object
print(list1 is list2)  # Both have the different objects


#############

#Assignment Operators#
#This is a category of operators which is used to assign values to a variable

# Operator 	        Purpose 	        Notation
# = 	            Assign 	            In-fix
# += 	        Add and Assign      	In-fix
# -=    	Subtract and Assign 	    In-fix
# *=    	Multiply and Assign     	In-fix
# /=    	Divide and Assign 	        In-fix
# //= 	Divide, Floor, and Assign   	In-fix
# **= 	Raise power and Assign      	In-fix
# %= 	Take Modulo and Assign 	        In-fix
# |= 	        OR and Assign       	In-fix
# &= 	        AND and Assign       	In-fix
# ^= 	        XOR and Assign       	In-fix
# >>= 	    Right-shift and Assign 	    In-fix
# <<= 	    Left-shift and Assign   	In-fix

#Variables are mutable, so we can change their values whenever we want!

year = 2019
print(year)

year = 2020
print(year)

year = year + 1  # Using the existing value to create a new one
print(year)

#One thing to note is that when a variable, first, is assigned to another variable, second, its value is copied into second.
# Hence, if we later change the value of first, second will remain unaffected:

first = 20
second = first
first = 35  # Updating 'first'

print(first, second)  # 'second' remains unchanged

#Some uses of the other Assignment Operators

num = 10
print(num)

num += 5
print(num)

num -= 5
print(num)

num *= 2
print(num)

num /= 2
print(num)

num **= 2
print(num)

num //= 2
print(num)

num %= 2
print(num)


#############

#Logical Operators#

# Operator 	 Purpose 	  Notation
# and          AND 	       In-fix
# or 	        OR 	       In-fix
# not          NOT 	       Prefix


#Logical Expressions#

#Logical expressions are formed using Booleans and logical operators.

# OR Expression
my_bool = True or False
print(my_bool)

# AND Expression
my_bool = True and False
print(my_bool)

# NOT expression
my_bool = False
print(not my_bool)


#Bit Value #

#In bit terms, the value of True is 1. False corresponds to 0:

print(10 * True)
print(10 * False)

#The Python interpreter can automatically convert the bool to its numerical form when needed.

#############

#Bitwise Operators#

#In programming, all data is actually made up of 0s and 1s known as bits. 
#Bitwise operators allow us to perform bit-related operations on values.

# Operator 	    Purpose 	    Notation
# & 	    Bitwise AND 	    In-fix
# | 	    Bitwise OR 	        In-fix
# ^ 	    Bitwise XOR 	    In-fix
# ~ 	    Bitwise NOT 	    Prefix
# << 	    Shift Bits Left 	In-fix
# >> 	    Shift Bits Right 	In-fix

num1 = 10  # Binary value = 01010
num2 = 20  # Binary Value = 10100

print(num1 & num2)   # 0   -> Binary value = 00000
print(num1 | num2)   # 30  -> Binary value = 11110
print(num1 ^ num2)   # 30  -> Binary value = 11110
print(~num1)         # -11 -> Binary value = -(1011)
print(num1 << 3)     # 80  -> Binary value = 0101 0000
print(num2 >> 3)     # 2   -> Binary value = 0010


#When performing the bitwise AND (&) operation, it takes the bit from num1 and the corresponding bit from num2 and performs an AND
#between them, this essentially is multiplication


   # num1 is 01010 in binary and num2 is 10100.
   # At the first step, the first binary digits of both numbers are taken:
        #    01010
        #    10100
    #0 & 1 would give 0 (again, think of it as multiplication).
    #Next, we take the second digits:
        #    01010
        #    10100
    #These two will once again give us 0.
    #Doing this for all pairs, we can see that the answer is 0 each time.
    #Hence, the output is 00000.

#When performing the OR operation, it works on the same principle, however it will be addition instead of multiplication

#0 OR 1 gives us 1.
# 1 OR 1 also produces 1 (binary numbers do not go beyond 1). 
# However, 0 OR 0 will give us 0 (0 + 0 is still 0).

#Bitwise XOR and NOT will work on each bit as well.

#The bitshift operations (>> and <<) simply move the bits to either the right or the left.
# When a binary number is shifted, a 0 also enters at the opposite end to keep the number of the same size.


#Examples of bitshift operations

#if we have 0110 >> 2
#we move it one step to the right to make 0011
#then we movie it one step to the right again to make it two bitsteps, this makes 0001
#this operation is now completed

#we can also do this to the left

#if we have 0110 << 2
#we move it one step to the left to make 01100
#then we movie it one more step to the left to make it two bitsteps, this makes 011000
#this operation is now completed

#the number 0011 will be equal to 11, but the number 00010111 will be equal to 10111.


#############

#String Operators#

#The string data type has numerous utilities that make string computations much easier.

#Strings are compatible with the comparison operators. Each character has a Unicode value.

#This allows strings to be compared on the basis of their Unicode values.

#When two strings have different lengths, the string which comes first in the dictionary is said to have the smaller value.

print('a' < 'b')  # 'a' has a smaller Unicode value (returns true)

house = "Gryffindor"
house_copy = "Gryffindor"

print(house == house_copy) #returns true

new_house = "Slytherin"

print(house == new_house) #returns false

print(new_house <= house) #returns false

print(new_house >= house) #returns true


#Concatenation#

#The + operator can be used to merge two strings together:


first_half = "Bat"
second_half = "man"

full_name = first_half + second_half
print(full_name)

#returns Batman!

#The * operator allows us to multiply a string, resulting in a repeating pattern:

print("ha" * 3)

#returns hahaha


#Search#

#The in keyword can be used to check if a particular substring exists in another string.
# If the substring is found, the operation returns true.

random_string = "This is a random string"

print('of' in random_string)  # Check whether 'of' exists in randomString... returns false as it isnt included in the string
print('random' in random_string)  # 'random' exists!... returns true as it is included in the string

