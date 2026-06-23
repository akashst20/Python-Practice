numbers = [5, 10, 5, 20, 10, 5]
freq = {}
for num in numbers:
    if num not in freq:
        freq[num] = 1
    else:
        freq[num] += 1
print(freq)
