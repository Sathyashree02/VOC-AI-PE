# BMI Calculator

# Get user input for height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the BMI result
print(f"Your BMI is: {bmi:.2f}")

# Determine the BMI category
if bmi <= 16:
    print("You are very underweight")
elif bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("Congrats! You are healthy")
elif bmi <= 30:
    print("You are overweight")
else:
    print("You are very overweight")
