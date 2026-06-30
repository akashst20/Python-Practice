sentence = input("Enter a sentence: ")
count = 0
for ch in sentence:
    if ch == " ":
        count += 1
if sentence != "":
    count += 1
print("The total number of words:", count)
