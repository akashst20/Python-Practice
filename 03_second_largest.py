numbers = [15, 60, 25, 90, 40]

largest = numbers[0]
second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num

    elif num > second:
        second = num

print("Largest:", largest)
print("Second Largest:", second)
