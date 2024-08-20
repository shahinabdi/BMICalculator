from bmi.bmi import BMI

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        bmi_calculator = BMI(weight, height)
        bmi_value = bmi_calculator.calculate()
        bmi_category = bmi_calculator.category()

        print(f"Your BMI is: {bmi_value:.2f}")
        print(f"You are classified as: {bmi_category}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()