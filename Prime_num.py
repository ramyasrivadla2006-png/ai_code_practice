a = int(input("enter a number: "))
if (a <= 1):
    print("not a prime number")
elif(a == 2):
    print(a," is a prime number")
else:
    if(a > 2):
        is_prime = True   
        for i in range(2,a):
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Prime")
        else:
            print("Not Prime")     