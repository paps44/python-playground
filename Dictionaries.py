"""Dictionaries in Phyton

We use dictionaries in phyton in situations where we need to store information that
comes as a key value pairs e.g. think of a customer, a customer has different attributes
like name, emails, phone each attributes has a value"""

#Name: Sonya Blade
#Email: sonya.blade@earthrealm.com
#Phone: 817654565

"""what we have above is a bunch of key value pairs"""
"""our keys are name, email & phone"""
"""each key is associated with a value: Sonya Blade, sonya.blade@earthrealm.com, 817654565 """

customer = {
    "name": "Sonya Blade",               #a string
    "age": 30,                           #a number
    "is_verified": True                  #bullion, list or anything
}
print(customer["name"])

"""what if we pass a key that doesn't exist """

customer = {
    "name": "Sonya Blade",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Sergent Jax"
print(customer["name"])

"""Exercise: Program to perform phone number to words"""

phone = input("phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}
output = ""
for fig in phone:
    output += digits_mapping.get(fig, "!") + " "
print(output)

