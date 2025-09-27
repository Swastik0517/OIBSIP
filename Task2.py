print("\n===BODY MASS INDEX (BMI) CALCULATOR===\n")

def calculate_bmi(weight, height):
    return weight / ((height*0.3048) ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "High BMI"   

def main():
    try:
        weight = float(input(" Enter your weight (in kilograms): "))
        height  = float(input(" Enter your height (in feet): "))

        if weight <= 0 or height <= 0:
            print("\nInvalid entry! Height and weight must be positive numbers.")
            return

        bmi_value = calculate_bmi(weight, height)
        category = bmi_category(bmi_value)

        print(f"Your BMI is: {bmi_value:.2f}")
        print(f"Category : {category}")

    except ValueError:
        print("\nError: Please enter numeric values only.")

if __name__ == "__main__":
    main()
