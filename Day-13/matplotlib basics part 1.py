import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 40]

plt.plot(x, y)#line graph
plt.bar(x, y)#bar graph
plt.scatter(x, y)#dot or scatter plot
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Sales Over Time")
plt.show()

marks = [35, 40, 45, 50, 52, 55, 60, 62, 65, 70, 75, 80, 85, 90]
plt.hist(marks,bins=5)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.grid()
plt.show()