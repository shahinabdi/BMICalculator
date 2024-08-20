class BMI:
    def __init__(self, weight: float, height: float):
        """
        Initialize the BMI calculator with weight (in kilograms) and height (in meters).
        """
        self.weight = weight
        self.height = height

    def calculate(self) -> float:
        """
        Calculate and return the BMI.
        Formula: BMI = weight (kg) / (height (m))^2
        """
        if self.height <= 0:
            raise ValueError("Height must be greater than 0")
        return self.weight / (self.height ** 2)

    def category(self) -> str:
        """
        Determine the BMI category based on the calculated BMI value.
        """
        bmi_value = self.calculate()

        if bmi_value < 18.5:
            return "Underweight"
        elif 18.5 <= bmi_value < 24.9:
            return "Normal weight"
        elif 25 <= bmi_value < 29.9:
            return "Overweight"
        else:
            return "Obesity"
