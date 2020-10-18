
name = input("Enter your name: ")
num = int(input("Enter a number between 1 an 5000 "))

if num >= 100 and num <= 500 or num >= 3000 and num <= 5000:
    print(name + " and " + str(num))
else:
    print(name + " and " + str(num) + " Not a match")