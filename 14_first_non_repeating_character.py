text=input("enter the string:")
freq={}
for ch in text:
    if ch not in freq:
        freq[ch]=1
    else:
        freq[ch]+=1
for ch in text:
    if freq[ch]==1:
        print("Frist non repeating character:",ch)
        break
      
