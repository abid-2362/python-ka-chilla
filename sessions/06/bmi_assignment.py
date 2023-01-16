# assignment
# Create a program to calculate your BMI

# BMI formula = (weight/height)^2
name = str(input("Enter your name: "))
weight = float(input(f'Hello {name}, please enter your weight in Kg: '))
height = float(input(f'Good Job {name}, please enter your height in meters: '))

BMI = (weight / height ** 2)
print(f'''Thank You {name},
Your BMI is: {BMI}''')

print(f'''BMI Categories:
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater ''')
