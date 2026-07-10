s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)
if(s == rev):
    print("palindrome")
else:
    print("no") 

