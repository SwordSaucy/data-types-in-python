box1 = {"sandwich,bacon,fries,juicebox,sandwich"}
box2 = {"biscuits,bacon,fries,sandwich,fries,bacon"}
box1.add("banana")
print(box1)
print(box1.intersection(box2))
import array as count
counts = count.array("i", [5, 423, 52 ,42, 85])
print(counts)
counts.insert(567,243)
counts.append(234)
print(counts)
print(counts.count(52))
counts.reverse()
print(counts)