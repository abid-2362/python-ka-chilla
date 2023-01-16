# assignment
# Create a program to calculate your BMI

# BMI formula = (weight/height)^2
name = str(input("Enter your name: "))
# weight = float(input("Helloy " + name + ", please enter your weight in Kg: "))
weight = float(input(f'Hello {name}, please enter your weight in Kg: '))
height = float(input(f'Good Job {name}, please enter your height in meters: '))

BMI = (weight / height**2)
print(f'Thank You {name},\n your BMI is: {BMI}')
