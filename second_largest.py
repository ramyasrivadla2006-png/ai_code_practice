n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
largest = second_large = arr[0]
for i in arr:
    if i > largest:
        second_large = largest
        largest = i
    elif i > second_large and i != largest:
        second_large = i
print("Second largest element is:", second_large)
