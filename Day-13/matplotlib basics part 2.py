import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 40]

plt.figure(figsize=(8, 5))

plt.plot(x, y)

plt.title("Sales")
plt.xlabel("Day")
plt.ylabel("Sales")

#subplot
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Bar")

plt.show()