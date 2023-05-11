from rich import print

# a. Open file without a context manager
filename = "show_version.txt"
f = open(filename)
data = f.read()
f.close()

print(f"\nData type: {type(data)}")
print("\nPrinting the first line to the screen: \n")
print("#" * 80)
print(data.splitlines()[0])
print("#" * 80)
print()

# b. Use a context manager
with open(filename) as f:
    data = f.readlines()

print(f"\nData type: {type(data)}")
print("\nPrinting the first line to the screen: \n")
print("#" * 80)
print(data[0].strip())
print("#" * 80)
print()
