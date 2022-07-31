#Now lets look at how to create functions that return values, this is useful doing
#calculation with function and we want to return result to whoever is using our F!

def square(number):
    return number * number

print(square(10))

#what if we don't use a return statement

def square(number):
    print(number * number)

print(square(10))

#we get 2 result on the terminal 100 & None, first phyton interpreter will call the square f!. By default all f!s returns the value none
#if we don't have a return statement by default phyton returns none
#None is an object that represents the absence of a value