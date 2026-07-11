#PATTERN 2
#n = int(input("Enter no.of rows: "))
#for i in range(1,n+1,+1):
#for j in range(n-i):
#print(" ",end = " ")
#for k in range(i):
#print("*",end =" ")
#print()

#pattern3
#n= int(input("enter no of rows: "))
#for i in range(1,n+1):
#for j in range(i):
#print("*",end = " ")
#print()
#for r in range(1,n,+1):
#for b in range(n-r):
#print("*",end =" ")
#for a in range(r):
#print(" ",end =" ")
#print()

#PATTERN 4
#n= int(input("enter "))
#for i in range (n):
#for j in range(n):
#if (i == j or i+j == n-1):
#print("*",end =" ")
#else:
#print(" ",end=" ")
#print()

#PATTERN 4
#SQUARE BORDER
#n= int(input("enter no of rows: "))
#for i in range(n):
#for j in range(n):
#if( j==0 or j==n-1 or i==n-1 or i==0):
#print("*",end=" ")
#else:
#print(" ",end=" ")
#print()

#PATTERN 5 ---UR NAME FIRST LETTER
n = int(input("enter no of rows: "))
for i in range(n):
    for j in range(n):
        if((i==0 and  j!=n-1) or (i==1 and (j==0 or j==4)) or (i==2 and j!=n-1) or (i==3 and (j==0 or j==2)) or (i==4 and (j==0 or j==3))):
            print("*",end=" ")
        else:
            print(" ",end =" ")
    print()
