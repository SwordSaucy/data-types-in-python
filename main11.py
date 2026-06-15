decimal_number = int(input("Enter a decimal number to convert: "))
original_number = decimal_number
if decimal_number == 0:
    binary_string = "0"
else:
    binary_string = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_string = str(remainder) + binary_string
        decimal_number = decimal_number // 2  
print("The decimal number", original_number, "in binary is:", binary_string)