largest = None
smallest = None
n = []
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else:
        try:
            n.append(int(num))
        except:
            print("Invalid input")
for i in n:
    if smallest is None or largest is None:
        smallest = i
        largest = i
    elif i > largest:
        largest = i
    elif i < smallest:
        smallest = i

print("Maximum is", largest)
print("Minimum is", smallest)
