height=float(input("enter the height\n"))
weight=float(input("enter the weight\n"))
bmi=weight/height**2
if bmi<18.5:
    print(f"your BMI is{bmi},you are underweight.")
elif bmi>=18.5:
    print(f"your BMI is {bmi},you have normal weight.")
elif bmi>=25 and bmi<30:
    print(f"your BMI is {bmi},you are slightly overweight.")
elif bmi>=30 and bmi<35:
    print(f"your BMI is {bmi},you are obese.")
else:
    print(f"your BMI is {bmi},you are clinically obese")