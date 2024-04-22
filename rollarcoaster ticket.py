height=int(input("what is your height"))
if height>120:
    age=int(input("enter your age"))
    if age<12:
        fee=5
    elif age<18:
        fee=7
    else:
        fee=12
    photo=input("do you want photos Y or N")
    if photo=="Y":
        fee=fee+3
    print(f"you can ride, the fees is {fee}")
else:
    print("you can't ride")
