myset = {1,1,1,1,2,2,3,3,3,3,4}
print(myset)

myset.add(5)
print("Updated: ",myset)

set1 = myset
set2 = {2,4,4,6}

print("Set1: ", set1)
print("Set2: ", set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric difference")
print(set1.symmetric_difference(set2))