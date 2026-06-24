numbers = [70, 20, 50, 10, 40]
n=len(numbers)
for i in range(n-1):
    for j in range(n-1-i):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print(numbers)
