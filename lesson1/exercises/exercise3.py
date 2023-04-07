line = "Processor board ID FAL127990LA"

# _ indicates a 'junk' variable
_, _, _, serial_number = line.split()
print("\nCall .split() and assign output to four variables:")
print(serial_number)

# Python3 also allows you to do list unpacking here.
# The 'serial_number' var will get assigned one element (the last one)
# the *junk will create a list named 'junk'  and put as many things into
# as required to make the unpacking work (in this case three elements)
print("\nCall .split() and assign output to a list and a variable:")
*junk, serial_number = line.split()
print(serial_number)

# You could also assign the .split() output straight to a list and retrieve
# the serial number from the list, but we haven't covered lists yet.
print("\nCall .split() and assign output to a list:")
words = line.split()
serial_number = words[-1]
print(serial_number)
