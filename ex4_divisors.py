num=int(input("Please provide a number: "))
print(" The list of its divisors:")
for i in range(1,num+1):
    if (num%i)==0:
        print(i)