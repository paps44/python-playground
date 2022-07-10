course ='''
   
   In this tutorial we are looking at formatted strings in Phyton Programming language.

   FS are peculiarly handy is situation where we dynamically generate text with our variables
   
   '''
print(course)

first = 'Martin'
last = 'Klepek'
message = first + ' [' + last + '] is a cloud manager.'
print(message)

first = 'Martin'
last = 'Klepek'
message = first + ' [' + last + '] is a cloud manager.'
msg = f'{first} [{last}] is a cloud manager.'
print(msg)