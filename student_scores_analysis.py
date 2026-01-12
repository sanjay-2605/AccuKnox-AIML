import matplotlib.pyplot as plt

students = {"A": 80, "B": 70, "C": 90}
avg = sum(students.values()) / len(students)
print("Average Score:", avg)

plt.bar(students.keys(), students.values())
plt.show()
