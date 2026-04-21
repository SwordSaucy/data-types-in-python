sellingprice = int(input("enter the price of the item being sold: "))
originalprice = int(input("enter the price of the item originally: "))
if originalprice > sellingprice: 
    c = originalprice - sellingprice
    print("you are losing money from selling this item and you are losing" + str(c))
elif sellingprice > originalprice: 
    b = sellingprice - originalprice
    print("you are getting profit from selling this item and you are getting " + str(b))
else: 
    print("you are not getting any money from selling this item/ you are getting 0£ from selling this item")