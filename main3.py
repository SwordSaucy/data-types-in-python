class pairelements:
    def twosum(self,number,target):
        lookup = {}
        for i,num in enumerate(number):
            if target - num in lookup:
                return(lookup[target-num],i)
            lookup[num] = i
value = int(input("sum for which you want you make this search"))
print(f"index 1 = {pairelements().twosum((10,20,30,40,50),value)}")
            