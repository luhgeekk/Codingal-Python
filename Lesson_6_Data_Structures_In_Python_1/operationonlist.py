fruits = ["Dates" , "Bananas" , "Apples" , "Oranges" , "Kiwis"]

print("Length of list:" , len(fruits))
print("First Element:" , fruits[0])
print("Last Element:" , fruits[-1])

fruits.append("Tamarinds")
print("Updated List:" , fruits)

fruits.remove("Apples")
print("Updated List:" , fruits)

fruits.sort()
print("Sorted List:" , fruits)

fruits.reverse()
print("Reversed List:" , fruits)

print("Multiplication on List:" , fruits*5)

fruits = fruits[:4]
print("Sliced List:" , fruits)

fruits.clear()
print("Cleared List:" , fruits)