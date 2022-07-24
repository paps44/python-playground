#Let's take a look at how list works and play around with it.

names = ['Nepal', 'Prague', 'Germany', 'United States', 'Lagos', 'United Kingdom']
print(names)

#What we see on the terminal looks exactly as we have defined our list.
#So we have six strings in this list. We can also access an individual element
#using an index just like how we can access individual character in a string
#using an index.

names = ['Nepal', 'Prague', 'Germany', 'United States', 'Lagos', 'United Kingdom']
print(names[1])

names = ['Nepal', 'Prague', 'Germany', 'United States', 'Lagos', 'United Kingdom']
print(names[3])

names = ['Nepal', 'Prague', 'Germany', 'United States', 'Lagos', 'United Kingdom']
print(names[-1])

names = ['Nepal', 'Prague', 'Germany', 'United States', 'Lagos', 'United Kingdom']
print(names[-4])

names = ['Nepal', 'Prague', 'Germany', 'United States', 'Lagos', 'United Kingdom']
print(names[2:])

names = ['Nepal', 'Prague', 'Germany', 'United States', 'Lagos', 'United Kingdom']
print(names[2:5])

names = ['Nepal', 'Prague', 'Germany', 'United States', 'Lagos', 'United Kingdom']
print(names[:])

names = ['Nepal', 'Prague', 'Germany', 'United States', 'Lagos', 'United Kingdom']
print(names[1])
print(names)

#We can also modify any of the elements in this list. For instance let's say we
#made a mistake and the first item shouldn't be Nepal with a N, so we want to remove the N

names = ['Nepal', 'Prague', 'Germany', 'United States', 'Lagos', 'United Kingdom']
names[0] = 'Lepal'
print(names)

#Exercise = Write a program to find the largest number in a list.

numbers = [4, 7, 3, 9, 6, 8, 10, 40]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#So lets take it further by finding the minimum number in a list.

numbers = [4, 7, 3, 9, 6, 8, 10, 40]
min = numbers[0]
for number in numbers:
    if number < min:
        min = number
print(min)