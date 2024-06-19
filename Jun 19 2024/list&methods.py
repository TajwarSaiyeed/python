l1 = [1,2,3,4,5, "Abid", 3]
# print(type(l1)) <class 'list'>
print(l1) # [1, 2, 3, 4, 5, 'Abid']

l1.remove("Abid")
print(l1)

print(l1.count(3)) # 2

l1.sort() # asc
# l1.sort(reverse=True) # desc
print(l1) # [1, 2, 3, 3, 4, 5]

l1.append(50)
print(l1) # [1, 2, 3, 3, 4, 5, 50]

# l1.clear()
# print(l1) [] <- clear the list

l1.extend([10, 5, 25, 95])
l1.sort()
print(l1) # [1, 2, 3, 3, 4, 5, 5, 10, 25, 50, 95]

l2 = l1.copy()
print("l2 => ", l2)
# print(l1.index(20)) # ValueError: 20 is not in list
print(l1.index(50)) # 9
l1[9] = 20
print(l1)