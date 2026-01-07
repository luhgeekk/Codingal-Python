mytuple = ()
print(mytuple)

mytuple = (1,2,3)
print(mytuple)

mytuple = (1, "Hello", 3.6)
print(mytuple)

mytuple = ("hi" , [1,2,4,5], (1,7,6,8,9))
print(mytuple)

mytuple = ('p','e','r','m','i','t')
print(mytuple[0])
print(mytuple[5])

nestedtuple = ("hi" , [1,2,4,5], (1,7,6,8,9))
print(nestedtuple[0][1])
print(nestedtuple[2][2])

print("Sliced: ",mytuple[2])

for letter in mytuple:
    print("Hello, ",letter)