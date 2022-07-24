#Two dimensional lists are extremely powerful and they have a lot of
#applications in data science and machine learning.

'''A 2 dimensional list is a list where each item in that list has another list'''


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0][1])

#We can also use nested loop to
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)



