n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
a =int(input("enter an element u want to search : "))
found = False
for i in range(len(arr)):
    if a==arr[i]:
        print(" the element",a, "is found at index",i)
        found = True
        break
if found == False:
    print("Element is not found in array")
