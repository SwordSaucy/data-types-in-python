countrycode = {"india":"0091","austrailia":"0025","nepal":"00977"}
a = input("enter the country here: ")
for i,j in countrycode.items():
    if i == a:
        print(j)
else:
    print("not found")