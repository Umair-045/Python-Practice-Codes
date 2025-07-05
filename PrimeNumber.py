n = int(input("Enter Number :"))

if n<=1:
    print("It is not a prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("it is not a prime number")
            break
    else:
        print("Prime Number")
        