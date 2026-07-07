def calculate_change(total_bill, amount_paid):

    change = amount_paid - total_bill

    return change


vishals_change = calculate_change(2.5, 4)

print(f"The shopkeeper should return: ${vishals_change}")