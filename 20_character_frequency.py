text=input("Enter the string:")
freq={}
for i in text:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("The frequency of each character in the string is :",freq)
