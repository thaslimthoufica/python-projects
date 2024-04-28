name1=input("enter first person name:")
name2=input("enter second person name:")
name=name1+name2
lowercase=name.lower()
t=lowercase.count("t")
r=lowercase.count("r")
u=lowercase.count("u")
e=lowercase.count("e")
first_digit=t+r+u+e
l=lowercase.count("l")
o=lowercase.count("o")
v=lowercase.count("v")
e=lowercase.count("e")
second_digit=l+o+v+e
love=(str(first_digit)+str(second_digit))
print(f"YOUR LOVE SCORE IS: {love}")
