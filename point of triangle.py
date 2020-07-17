print("Upper left corner coordinate:")
x1 = int(input("  << x axis: "))
y1 = int(input("  << y axis: "))
east = int(input("  << Eastern: "))
south = int(input("  << Southern: "))
print("Enter a coordinate:")
x2 = int(input("  << x axis: "))
y2 = int(input("  << y axis: "))

a = x1 + east
b = y1 - south

if x2 <= a and x2 >= x1 and y2 >= b and y2 <= y1:
print(">>> (%.2f, %.2f) is inside the rectangle." %(x2,y2))
else:
    print(">>> (%.2f, %.2f) is not inside the rectangle." %(x2,y2))