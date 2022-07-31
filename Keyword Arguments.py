#from the last practice we learnt that whenever we define parameters(first_name, last_name)
#for our F!s we should always supply values otherwise we"ll get an error

#For the most part use positional argument.

#Keyword argument improves the readability of our codes, Keyword arguments should always
#come after positional argument

#if you're passing both positional and keyword arguments, use the keyword argument after
#the positional arguments.

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")

print("Start")
greet_user("Don Luigi", last_name="Smith")
print("Finish")