number=int(input("Please provide a number: "))

if (number%2) == 0:
    print("The number " + str(number) + " is even!")
else:
    print("The number " + str(number) + " is odd!")

if (number%4) == 0:
    print("The number " + str(number) + " is a multiple of 4!")

print(30*"#")
num=int(input("Please provide a number: "))
check=int(input("Please provide an other number: "))

if (num%check)==0:
    print("The number " + str(num) + " is a evenly devided by " + str(check))
else:
    print("The number " + str(num) + " is a not evenly devided by " + str(check))

