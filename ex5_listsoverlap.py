import random

l2=[]
l3=[]
l4=[]
for i in range(0,100):
    l2.append(random.randint(1,21))
print("L2("+ str(len(l2))+"):\n" + str(l2))
print(40* "#")


for i in range(0,15):
    l3.append(random.randint(1,21))
print("L3("+ str(len(l3))+"):\n" + str(l3))
print(40* "#")

for element2 in l2:
    for element3 in l3:
        if element2==element3:
            l4.append(element2)
            break
        
print("L4("+ str(len(l4))+"):\n" + str(l4))



