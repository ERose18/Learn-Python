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

