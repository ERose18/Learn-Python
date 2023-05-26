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

