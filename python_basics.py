#ass1_problems
#1....
#age=int(input("enter age: "))
#name=input("enter name: ")
#print("hello",name,"you are",age," years old")

#2..
#a=int(input("enter integer: "))
#b= int(input("enter integer: "))
#c= float(input("enter decimal num: "))
#print(float(a),float(b),c)

#3..
#a=input("enter:")
#print(float(a),type(float(a)))
#print(int(a),type(int(a)))
#print(a,type(a))

#4..
#a=10+3*2**2
#print(a)

#5...
#a=5
#b=6
#temp=a
#a=b
#b=temp
#print(a,b)

#6..
#c=int(input("enter celsius val: "))
#cel=float(c)
#farh=((cel) * (9/5)) +32
#print(farh)

#7...
#a=float(input("enter num:" ))
#print(int(a))
#print(float(a) - int(a))

#multiplication table
#n=int(input("enter the num which u want a table: "))
#i=1
#while (i<11):
#print(n,"x",i,"=",n*i)
#i += 1

word ="ARTIFICIAL INTELLIGENCE"
count = 0
for var in word:
    if(var == "I" or var == "A" or var == "E" or var =="O" or var == "U"):
       count += 1
print(count)

d=int(input("enter num:"))
sum = 0
for i in range(1,d+1):
    sum += i
print(sum)



