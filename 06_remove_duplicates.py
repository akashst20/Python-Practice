numbers = [10, 20, 10, 30, 20]
new=[]
for num in numbers:
  if num not in new:
    new.append(num)
print(new)
