#How to Handle Error in Python Program

age = int(input("Age: "))
print(age)

#the exit code 0 means our program terminated successfully with no errors
#An exception is kind of error that crashes our program

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")

#to cover another kind of error in our program

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value")