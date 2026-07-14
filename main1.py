store = {"mark1":44,"mark2":34,"mark3":86,"mark4":54,"alex":32}
score = []
sum = 0
for key,value in store.items():
    score.append(value)
    sum = sum + value
maxdw = max(score)
mindw = min(score)
for key,value in store.items():
    if maxdw == value:
        print(f"the maximum score is {maxdw} and is scored by {key}")
    if mindw == value:
        print(f"the minimum score is {mindw} scored by {key}")
average = sum / len(score)
print(f"the average of all the scores is {average}")
new = (input("enter a new name you want to search!: "))
newscore = store.get(new)
print(f"the score of {new} was {newscore}")
if new not in store:
    print(f"{new} is not in the store")