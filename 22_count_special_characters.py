text=input("Enter the sring :")
count=0
for i in text:
    if not i.isalnum() and not i.isspace():
        count+=1
print("The number of special characters in the string is :",count)
