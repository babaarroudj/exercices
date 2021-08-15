a = []
print("Please provide ten numbers: ")
for i in range(1,11):
    a.append(int(input()))

print("You provided the following list: " + str(a))

print(40*"#")

print("\n The numbers that are lesser than 5 are: ")
for element in a:
    if element < 5:
        print(element)