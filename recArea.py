L1 = int(input("Enter length of a rectangle: "))
W1 = int(input("Enter width of a rectangle: "))

L2 = int(input("Enter length of another rectangle: "))
W2 = int(input("Enter width of another rectangle: "))

area1 = L1 * W1
area2 = L2 * W2

if area1 > area2:
    print("Rectangle 1 is bigger")
elif area2 > area1:
    print("Rectangle 2 is bigger")
elif area1 == area2:
    print("Both rectangles are the same size")
else:
    print("Cannot compute")