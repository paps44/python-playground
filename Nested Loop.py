#Nested loop in Python basically means adding one loop inside, of another loop.
#for instance, we can  generate coordinates.

for x in range(4):
    for y in range(3):
        print (f'({x}, {y})')

'''
#Challenge
#Cheating with special features in python
'''
numbers = [5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)


numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#Taking it further to write letter L

numbers = [1,1,1,5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)