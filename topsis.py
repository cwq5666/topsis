import numpy as np
print("请输入参评数目")
n = int(input())
print("请输入评价指标数目")
m = int(input())


# 输入
print("请输入kind矩阵:1,极大型2，极小，3，中间，4，区间")
kind = input().split(" ")

print("请输入矩阵")
A = np.zeros((n,m))
print(A)
for i in range(n):
    A[i] = input().split(" ")
    A[i] = list(map(float,A[i]))#将字符串转化为浮点数列表
print("输入矩阵为：\n",format(A))
    