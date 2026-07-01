n=int(input("Enter a number:"))
reverse=0
original = n
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if reverse==original:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
