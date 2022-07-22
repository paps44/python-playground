#we learnt that we use while loop to execute a block of codes multiple times

#For loops is used iterate items of a collection, such as a string.
#A string is a sequence of characters, so it looks like a collection so a
#for loop can be used to iterate over each character string and the do something with it.

for item in "Germany":
    print(item)

for item in range (5, 10, 2):
    print(item)

for item in range (100):
    print(item)

#Exercises
#Calculate the prices of goods in a shopping cart

prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"total: {total}")

