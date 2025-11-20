# Prompt user for input
temp_f = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
temp_c = (temp_f - 32) * 5 / 9

# Display Celsius value
print(f"Temperature in Celsius: {temp_c:.1f}")

# Decide water state using if/elif/else
if temp_c <= 0:
    print("Ice")
elif temp_c > 0 and temp_c < 100:
    print("Liquid")
else:
    print("Gas")

# Prompt user for number of packages
num_packages = int(input("Enter # of packages to ship: "))

# Prompt for shipping type
shipping_type = input("Enter r for regular, e for express: ")

# Decide rate using if/else
if shipping_type == "r":
    rate = 10
else:
    rate = 15

# Calculate total cost
total_cost = num_packages * rate

# Display result with formatting
print(f"Total cost: $ {total_cost}")