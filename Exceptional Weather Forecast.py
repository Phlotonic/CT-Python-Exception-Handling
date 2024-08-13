# Task 1: Start
# Ask the user to enter the temperature in Fahrenheit
fahrenheit = input("Please enter the temperature in Fahrenheit: ")

# Task 2: Temperature Conversion
def convert_to_celsius(fahrenheit):
    try:
        # Convert the input to a float
        fahrenheit = float(fahrenheit)
        # Convert Fahrenheit to Celsius using the formula
        celsius = (fahrenheit - 32) * 5/9
    except ValueError:
        # Handle the case where the input is not a number
        print("Invalid input! Please enter a numeric value.")
    else:
        # Task 3: User Experience
        # Print the converted temperature in a user-friendly format
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        # Task 4: Finally
        # Thank the user for using the weather forecast application
        print("Thank you for using the weather forecast application.")

# Call the function to perform the conversion
convert_to_celsius(fahrenheit)
