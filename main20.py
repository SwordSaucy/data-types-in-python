habit_info = ("hello", True, 32, 675.8)
weekly_habit = (0, 1, 0, 1, 0, 1, 0)

length = len(weekly_habit)
print(f"the amount of days there are here are {length}")
print(f"weekly habit (1): {weekly_habit[0]}")
print(f"weekly habit (2): {weekly_habit[1]}")

print(f"the days of 3 to 5: {weekly_habit[2:5]}")

weekly_habit = weekly_habit + (1,)
print(weekly_habit)

one = 0
zero = 0

for i in weekly_habit:
    if i == 1:
        one = one + 1
    if i == 0:
        zero = zero + 1

print("completed = ", one)
print("not completed = ", zero)

if one > zero:
    print("good job")
else:
    print("bad job!")