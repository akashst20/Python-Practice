text=input ("Enter the string:")
count=0
for i in text:
    if i.isalpha() and i not in "aeiouAEIOU":
        count+=1
print("The total number of consonants:",count)
