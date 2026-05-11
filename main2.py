# calculate electricity bill , number of units consumed and number. if units is less than 50 then bill 2.60per unit and tax is 25 .if units is less than 100 then bill is 3.5 per unit and tax is 30.if units is less than 200 then bill 5.26it and tax is 45.else per unit cost is 8.45 and tax is 75
a = int(input("please enter the amount of units bought: "))
if a <= 50: 
    print(a*2.60+25)
elif a <= 100: 
    bill = (50*2.6)+((a-50)*3.5)+30
    print("your bill is", bill )
elif a <= 200: 
    bill1 = (50*2.6)+(50*3.5)+((a-100)*5.26)+45
    print("your bill is". bill1 )
else: 
    bill2 = (50*2.6)+(50*3.5)+(100*5.26)+((a-200)*8.45)+75
    print("your bill is", bill2 )