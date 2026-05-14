#BMI Calculator

def calculate_bmi(weight, height_cm):

    # Convert cm to meters
    height_m = height_cm / 100

    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


try:

    weight = float(input("Enter your weight in kg: "))
    height_cm = float(input("Enter your height in cm: "))

    if weight <= 0 or height_cm <= 0:
        print("Please enter positive values.")

    else:
        bmi = calculate_bmi(weight, height_cm)
        category = bmi_category(bmi)

        print("\n----- BMI RESULT -----")
        print("BMI:", bmi)
        print("Category:", category)

except ValueError:
    print("Invalid input! Please enter numbers only.")
