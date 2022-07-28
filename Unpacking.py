"""Unpacking is a powerful feature in python

"""

coordinates = (1, 2, 3)    #A tuple
#x = coordinates [0]
#y = coordinates [1]
#z = coordinates [2]

"""Instead of repeating coordinates of 2 or coordinates of 0 multiple times,
 we can simply work with the variables below called unpacking with that
 same result can be achieved with far less codes"""

x, y, z = coordinates          #this is a shorthand to achieve same result above. How it works is that when phyton interpreter sees this statement
print(y)                       #it will get the 1st item in the tuple & assign it to the variable & thus the sequence.
                               #So we are unpacking the tuple into 3 variables

#This is not limited to tuples we can use it in list as well.

coordinates = [1, 2, 3]
x, y, z = coordinates
print(y)



