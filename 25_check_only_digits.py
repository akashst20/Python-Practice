string = input("Enter a string: ")
for ch in string:
    if not ch.isdigit():
        print("The string contains non-digit characters.")
        break
else:
    print("The string contains only digits.")
