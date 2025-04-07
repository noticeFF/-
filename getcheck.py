import numpy as np

def main(filename):
    with open(filename, 'r') as f:
        N = int(f.readline().strip())
        K = int(f.readline().strip())
        heights = np.array([int(f.readline().strip()) for i in range(N)])

    max_value = -10000001

    for i in range(N - K):
        for j in range(i + K, N):
            distance = heights[i] + heights[j] + (j - i)
            max_value = max(max_value, distance)

    return max_value
print("Максимальное значение для A.txt:", main("A.txt"))
print("Максимальное значение для B.txt:", main("B.txt"))
