def calculate_circumference(radius):
    circumference = 2 * 3.14 * radius
    return circumference
user_radius = float(input("Enter the radius of the circle in cm: "))
result = calculate_circumference(user_radius)
print("The circumference of the circle is:", result)