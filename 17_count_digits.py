text=input("Enter the string :")
count=0
for i in text:
    if i.isdigit():
        count+=1
print("The total number of digit:",count)
