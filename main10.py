
decimal = int(input("Enter a decimal number to convert: "))
original_number = decimal
if decimal == 0:
    binary = "0"
else:
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
print("The decimal number", original_number, "in binary is:", binary)