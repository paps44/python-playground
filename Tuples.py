#tuples are similar to list, so we can use them to store a list of items
#but unlike list we cannot modify them, we cannot add new items, we cannot remove
#existing items, tuples are immutable i.e. we cannot mutate or change them

numbers = (1, 2, 3)    #tuples are created with parenthesis
print(numbers[0])       #lists in tuples only have 2 options count & index
                        #count is to count the occurrence of an items, index to find the index of the first occurrence of an item

numbers = (1, 2, 3)
numbers[0] = 10
print(numbers[0])

#Practically most of the time list will be used but tuples are also useful to make sure
#no where in our program we accidentally modify a particular list, then it's good
#practise to use a tuple