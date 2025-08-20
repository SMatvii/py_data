import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
result1 = np.hstack((a1, a2))
print("Завдання 1:", result1)

array = np.array([12, -5, 7, 9, -3, 15])
result2 = np.append(array, 10)
print("Завдання 2:", result2)

matrix = np.array([
    [5, 2, 8],
    [1, 7, 4],
    [3, 6, 9]
])
result3 = np.delete(matrix, 1, axis=0)
print("Завдання 3:\n", result3)
