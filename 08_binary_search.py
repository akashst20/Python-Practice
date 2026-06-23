numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]
target = 30
low = 0
high = len(numbers) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if target == numbers[mid]:
        print("Found at index", mid)
        found = True
        break
    elif target < numbers[mid]:
        high = mid - 1
    else:
        low = mid + 1
if not found:
    print("Not Found")
