num = int(input("Enter number to be checkd for prime/not prime: "))
flag = False

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print("The number is not a prime")
else:
    print("This number is a prime number")2


