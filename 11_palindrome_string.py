name=input("enter the string:")
reverse=""
for i in range(len(name)-1,-1,-1):
    reverse+=name[i]
if reverse==name:
    print("palindrome")
else:
    print("Not palindrome")
    
