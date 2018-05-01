import matplotlib.pyplot as plt
import fibonacci

# Set lists to X and Y axis.
plt.plot(fibonacci.listX, fibonacci.listY)

# Label axis and title.
plt.xlabel('Steps')
plt.ylabel('Fibonacci Value')
plt.title('Visualisation of Fibonacci Sequence')

plt.show()
