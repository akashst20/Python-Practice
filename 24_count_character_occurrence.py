text=input("Enter a string:")
check=input("Enter a character to check its occurrence:")
count=0
if len(check)!=1:
    print("please enter a single character to check its occurrence")
else:
    for i in text:
        if i==check:
            count+=1
    print("The character '{}' occurred {} times in the string.".format(check,count))
