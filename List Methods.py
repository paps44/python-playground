#let's look at the operations that can be performed in a list
#there are a number of things we can do on a list
#1. we can add new items to it
#2. we can remove existing items
#3. we can check the existence of an item

numbers = [4, 8, 3, 6, 2, 16, 9]
numbers.append(21)
print(numbers)

#what if we want to add a number somewhere in the middle or at the beginning of the list?
#that is called insert

numbers = [4, 8, 3, 6, 2, 16, 9]
numbers.insert(0, 21)
print(numbers)

#So let's remove an item from the list

numbers = [4, 8, 3, 6, 2, 16, 9]
numbers.remove(6)
print(numbers)

#if we want to remove all the items in the list we can use clear

numbers = [4, 8, 3, 6, 2, 16, 9]
numbers.clear()
print(numbers)

#we can also remove the last item on a list

numbers = [4, 8, 3, 6, 2, 16, 9]
numbers.pop()
print(numbers)

#we can also check the existence of an item on a list with index

numbers = [4, 8, 3, 6, 2, 16, 9]
print(numbers.index(8))

#numbers = [4, 8, 3, 6, 2, 16, 9]
#print(numbers.index(21))

#there is also another way to check a character or a sequence of character in a list
#we will get a bullion value True/False

numbers = [4, 8, 3, 6, 2, 16, 9]
print(21 in numbers)

numbers = [4, 8, 3, 6, 2, 16, 9]
print(16 in numbers)

#we also have another method for counting the occurrences of an item

numbers = [4, 8, 3, 9, 6, 2, 16, 9]
print(numbers.count(9))

#If we want to sort a list we can call the sort method

numbers = [4, 8, 3, 6, 2, 16, 9]
numbers.sort()
print(numbers)
#sorted in ascending order

#Now lets sort in descending order

numbers = [4, 8, 3, 6, 2, 16, 9]
numbers.sort()
numbers.reverse()
print(numbers)

#Another method is the copy list

numbers = [4, 8, 3, 6, 2, 16, 9]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)

#Exercise: write a program to remove the duplicates in a list
numbers = [4, 8, 3, 9, 6, 2, 16, 9, 12, 6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)