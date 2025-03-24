def task(name):
    with open(name, 'r') as file:
        n = int(file.readline().strip())
        k = int(file.readline().strip())
        heights = [int(file.readline().strip()) for i in range(n)]
    maximum = 0
    for i in range(n-k+1):
        for j in range(n+k-1):
            summ = heights[i] + heights[j] + ((j-1)*1000)
            maximum = max(maximum,summ)
    print("Максимальное значение = ", maximum)

task("A.txt")
task("B.txt")