print("This program displays a list of numbers")
print("Starting at 1 and their squares")
start = int(input("Where should I begin? "))
end = int(input("How high should I go? "))

print()
print("Number\tSquare")
print('--------------')

for num in range(start, end + 1):
    square = num ** 2
    print(num, '\t', square)