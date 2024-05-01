def get_input():
    height = float(input("Enter height: "))
    weight = float(input("Enter weight: "))
    return height, weight


def metric_units(weight, height):
    bmi = weight/(height*height)
    print(f"BMI is {bmi}.")
    return bmi

def imperial_units(weight, height):
    bmi = 703 * (weight/(height*height))
    print(f"BMI is {bmi}.")
    return bmi

print("Disclaimer: Metric system uses height in meters and weight in kgs. \n")
print("Imperial systems uses height in inches and weight in pounds. \n")       

sel = int(input("Choose between; 1. Metric system 2. Imperial system: "))

height, weight = get_input()


if sel == 1:
    bmi = metric_units(weight, height)

elif sel == 2:
    bmi = imperial_units(weight, height)

else :
    print("Invalid input!")

if bmi < 0:
    print("Invalid category.")

elif bmi > 0 and bmi <= 18.4:
    print("Underweight.")

elif bmi == 18.5 and bmi <=24.9:
    print("Normal.")


elif bmi ==25 and bmi <=39.9:
    print("Overweight.")

else:
    print("Obese.")
