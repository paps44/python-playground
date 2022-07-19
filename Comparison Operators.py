# Comparison operators are used when we want to compare a variable with a value
# for example

#CONDITIONS
#if temperature is greater than 30
    #it's a hot day
#otherwise if it's' less than 10
    #it's a cold day
#otherwise
    #it's neither hot nor cold

temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#COMPARE

temperature = 35

if temperature > 30: #bullion expression >,<,=,==,!=
    print("It's a hot day")
else:
    print("It's not a hot day")

#EXERCISE

name = "J"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("name must be a maximum of 50 characters")
else:
    print("Name looks good!")

name = "Jeytyweoiytiyhgdkjghsahsgueytbvxznpwrtvxzmmayooerrwrrrrradfttfammaffaaffrrwacxpqal"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("name must be a maximum of 50 characters")
else:
    print("Name looks good!")

name = "Ariyo Adebayo Simeon"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("name must be a maximum of 50 characters")
else:
    print("Name looks good!")
