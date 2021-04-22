def calculate_miles_per_gallon(miles_driven, gallons_used):
    mpg = miles_driven / gallons_used
    mpg = round(mpg, 1)
    return mpg


miles = 500
gallons = 14
print(calculate_miles_per_gallon(miles, gallons))


def welcome(message):
    print(message)
    print()


message = "Welcome to this tiny function"
welcome(message)

