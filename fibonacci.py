# Get the amount of steps desired from the user.
steps = int(input("Enter how many steps you wish you calculate"))
steps += 1

# X axis (Steps)
listX = []
# Y axis (Fibonacci number)
listY = []

# Pre append starting values to the X and Y axis lists.
a = 0
b = 1
listX.append(a)
listX.append(b)
listY.append(a)
listY.append(b)

# Print steps 0 and 1 manually.
print("Step: 0 =", a)
print("Step: 1 =", b)

# Calculate Fibonacci sequence.
for i in range(2, steps):
    c = a + b
    a = b
    b = c
    print("Step:", i, "=", c)
    listX.append(i)
    listY.append(c)

# Print data points for X and Y axis.
print("\nX axis =", listX)
print("Y axis =", listY)
