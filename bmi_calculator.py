# ============================================================
#   BMI CALCULATOR - Oasis Infobyte Python Internship
#   Task 1: Beginner Level
#   Author: Yuvaraj.T.K
# ============================================================

# -------------------------------------------------------
# FUNCTION 1: Get a valid number from the user
# This function keeps asking until the user types
# A correct positive number (handles wrong input)
# -------------------------------------------------------
def get_positive_number(prompt):
    while True:                          
        try:
            value = float(input(prompt)) 
            if value <= 0:               
                print("❌ Please enter a positive number greater than 0.\n")
            else:
                return value             
        except ValueError:               
            print("❌ Invalid input! Please enter a number only.\n")


# -------------------------------------------------------
# FUNCTION 2: Calculate the BMI
# Formula: BMI = weight (kg) / height (m) squared
# -------------------------------------------------------
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)         
    return round(bmi, 2)                 


# -------------------------------------------------------
# FUNCTION 3: Classify BMI into health categories
# Based on standard WHO BMI ranges
# -------------------------------------------------------
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "⚠️  You may need to gain some weight. Consult a doctor."
    elif 18.5 <= bmi < 25.0:
        return "Normal weight", "✅  Great! You have a healthy BMI. Keep it up!"
    elif 25.0 <= bmi < 30.0:
        return "Overweight", "⚠️  You may need to lose some weight. Consider diet & exercise."
    else:
        return "Obese", "🚨  Please consult a healthcare professional for guidance."


# -------------------------------------------------------
# FUNCTION 4: Display the result in a nice format
# -------------------------------------------------------
def display_result(weight, height, bmi, category, advice):
    print("\n" + "=" * 45)
    print("         📊  BMI CALCULATOR RESULT")
    print("=" * 45)
    print(f"  Weight        : {weight} kg")
    print(f"  Height        : {height} m")
    print(f"  Your BMI      : {bmi}")
    print(f"  Category      : {category}")
    print("-" * 45)
    print(f"  {advice}")
    print("=" * 45)


# -------------------------------------------------------
# FUNCTION 5: Show the BMI category chart
# -------------------------------------------------------
def show_bmi_chart():
    print("\n  📋 BMI Categories (WHO Standard):")
    print("  ----------------------------------")
    print("  Below 18.5   →  Underweight")
    print("  18.5 – 24.9  →  Normal weight")
    print("  25.0 – 29.9  →  Overweight")
    print("  30.0 & above →  Obese")
    print()


# -------------------------------------------------------
# MAIN PROGRAM - This is where everything runs
# -------------------------------------------------------
def main():
    print("=" * 45)
    print("    🏃 WELCOME TO BMI CALCULATOR 🏃")
    print("=" * 45)

    show_bmi_chart()                          

    while True:
        print("Enter your details below:")
        print("-" * 45)

        # Step 1: Get weight from user
        weight = get_positive_number("  Enter your weight (in kg)  : ")

        # Step 2: Get height from user
        height = get_positive_number("  Enter your height (in meters): ")

        # Step 3: Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Step 4: Classify BMI
        category, advice = classify_bmi(bmi)

        # Step 5: Display result
        display_result(weight, height, bmi, category, advice)

        # Step 6: Ask if user wants to calculate again
        print("\n  Do you want to calculate again?")
        again = input("  Type 'yes' to continue or 'no' to exit: ").strip().lower()

        if again != 'yes':
            print("\n  👋 Thank you for using BMI Calculator!")
            print("  Stay healthy! Goodbye.\n")
            break                             

        print("\n" + "-" * 45 + "\n")   


# -------------------------------------------------------
# This line runs the main() function when you execute
# the file. It's standard Python practice.
# -------------------------------------------------------
if __name__ == "__main__":
    main()
