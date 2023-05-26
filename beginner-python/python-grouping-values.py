#Grouping Values#

#we can store multiple values together in a single variable.
#While there are many ways of doing so, the most popular is the list.

#It is very similar to a string since a string is a collection of characters.
#A list is also just a collection of values. However, the values can be of any type.

#All you have to do is enclose all the elements in square brackets, [], and separate them with commas.

my_list = [1, 2.5, "A string", True]
print(my_list)

#Returns [1, 2.5, 'A string', True]


#Lists can be indexed and sliced just like strings. The len command works with them too:

my_list = [1, 2.5, "A string", True]
print(my_list[2])
print(len(my_list))

#Returns  A string (from my_list[2])  4 (the length of the string)

