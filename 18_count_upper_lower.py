text=input("Enter the string:")
countu=0
countl=0
for i in text:
    if i.isupper():
        countu+=1
    elif i.islower():
        countl+=1
print("The total number of upper case letters:",countu)
print("The total number of Lower case letters:",countl)
