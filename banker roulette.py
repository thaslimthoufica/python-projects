import random
n=int(input("enter the number of elements:"))
names=[]
for i in range(n):
    x=input("enter the names:")
    names.append(x)
random_name=random.randint(0,len(names)-1)
print(names[random_name] + " is going to buy meal")
