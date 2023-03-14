"""
a, Mã giả của thuật toán
procedure selectionSort(a: list of n elements)
    for i from 0 to n-1 do
        // tìm phần tử nhỏ nhất trong phần tử chưa được sắp xếp
        minIndex = i
        for j from i+1 to n-1 do
            if a[j] < a[minIndex] then
                minIndex = j

        // đổi chỗ phần tử nhỏ nhất với phần tử đang được sắp xếp
        if minIndex != i then
            swap(a[minIndex], a[i])
    end for
end procedure
b, Sở dĩ chỉ cần xét qua n-1 phần tử vì sau n-1 phần tử, phần tử cuối cùng luôn luôn là phần tử lớn nhất(Nhỏ nhất)
d, code dưới đây
"""
import random
import timeit
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Your statements here
time = []
with open('data.csv', 'w', newline='') as file:
    for n in range(10):
        start = timeit.default_timer()
        k = random.randint(1, 10000)
        A = random.sample(range(10000), k)
        for i in range(len(A)):

            # Tìm phần tử nhỏ nhất
            min_idx = i
            for j in range(i + 1, len(A)):
                if A[min_idx] > A[j]:
                    min_idx = j

            # Tráo phần tử nhỏ nhất với phần tử tại chỉ mục i
            A[i], A[min_idx] = A[min_idx], A[i]
        stop = timeit.default_timer()
        t = stop - start
        # chạy code
        row = [len(A), t]
        time.append([len(A), t])
        writer = csv.writer(file)
        writer.writerow(row)
data = pd.read_csv("data.csv")
# Show the description of data
data.describe()
y = np.array(data[1]).reshape(-1, 1)
x = np.array(data[0]).reshape(-1, 1)
plt.scatter(x, y)
plt.xlabel('n', fontsize=20)
plt.ylabel('Time', fontsize=20)
plt.show()