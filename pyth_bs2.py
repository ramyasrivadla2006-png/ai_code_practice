#num = int(input("enter a number: "))
#sal= int(input("enter your salary: "))
#if (sal > 70000):
#tot_sal=(sal *(100-25)/100)
#elif(sal > 30000 or sal<= 70000):
#tot_sal = (sal * (100-15)/100)
#else:
#tot_sal = (sal * (100-5)/100)
#print("your sal after tax is: ",tot_sal)

#a=int(input("first num: "))
#b= int(input("second num: "))
#i=a
#while i < b+1:
#if(i%2 == 0):
#print(i,"is a even number")
#i += 1

#n=int(input("enter num: "))
#sec = n%10
#sec2 = n/10
#sec3 = sec2%10
#sec4 = sec2/10
#print(int(sec)," ",int(sec3)," ",int(sec4)

#num = int(input("enter a number: "))
#def count_digits(num):
#ram =0
#while num>0:
#num = num//10
#ram += 1
#print("the no of digits is:",ram)
#count_digits(num)

#amm = int(input("enter n: "))
#def sum_of_n(amm):
#sum =0
#while amm >0:
#sum += amm %10
#amm = amm//10
#print("sum is: ",sum)
#sum_of_n(amm)

#for i in range(1,101):
#if(i%3== 0 and i%5==0):
#print(i)

#while (True):
#commd = input("lets start:")
#if(commd == "start"):
#n = int(input("enter a num"))
#if(n>0):
#print("postive number")
#elif(n<0):
#print("negative number")
#else:
#print("it is a zero")
#elif(commd == "quit"):
#print("program has been stopped")
#break         
    
n = int(input("enter a num: "))
if(n == 2):
    print(n,"is a prime number")
elif(n>2):
    for i in range(2,n-1):
        if(n % i == 0):
            print("not a prime")
            break
        else:
            print(n,"is a prime number")
            break
else:
    print("enter a number greater than 1")


