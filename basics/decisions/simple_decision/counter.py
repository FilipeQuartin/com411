first = int(input("Please enter the first whole number.\n"))
second = int(input("Please enter the second whole number.\n"))
third = int(input("Please enter the third whole number.\n"))
counter = 0
counter2 = 0
if (first % 2 == 0):
    counter = counter + 1
else:
    counter2 = counter2 + 1
if (second % 2 == 0):
    counter = counter + 1
else:
    counter2 = counter2 + 1
if (third % 2 == 0):
    counter = counter + 1
else:
    counter2 = counter2 + 1
print(f"There were {counter} even and {counter2} odd numbers.")