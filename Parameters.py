# the print function takes the information that we want to print for example
# print("Start")
# but our greet function doesn't take an information
# So let's look at how we can pass information to our function.
#def greet_user(inside this parenthesis we can add a parameter e.g. a name parameter):


def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard")

print("Start")
greet_user("Don Luigi")  #we can call this function one more time with a different name
greet_user("Lambdha")
print("Finish")

#arguement in programming is the value that we supply to a function
#referring to the above "Lambdha" is the argument we pass to the name parameter
#parameters are the hole or placeholders we define in our function for receiving information
#arguements are the actual pieces of information that we supply to these functions.

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")

print("Start")
greet_user("Don Luigi", "Smith")
print("Finish")