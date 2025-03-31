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


##定义各种函数
def mintomax(maxx,x):
    x = list(x)
    ans = [[maxx-i]for i in x]
    return np.array(ans)


def midtomax(best,x):
    x = list(x)
    h = [abs(best-i) for i in x]
    M = max(x)
    if M ==0:
        M = 1
    ans = [abs(1-i/M) for i in h]
    return np.array(ans)

def regtomax(low,high,x):
    x = list(x)
    M = max(low-min(x),max(x)-high)
    if M ==0:
        M = 1
    ans = []
    for i in range(len(x)):
        if x[i]< low:
            ans.append(1-(low-x[i])/M)
        elif x[i]>=low and x[i]<=high:
            ans.append(1)
        else:
            ans.append(1-(x[i]-high)/M)
    return np.array(ans)
##统一指标类型
X = np.zeros(shape = (n,1))
for i in range(m):
    if kind[i] == "1":
        V = np.array(A[:,i])
    elif kind[i] == "2":
        maxx = max(A[:,i])
        V = mintomax(maxx,A[:,i])
    elif kind[i] =="3":
        best = float(input("请输入最优值"))
        V = midtomax(best,A[:,i])
    else :
        print("输入区间")
        low = float(input("请输入下界"))
        high = float(input("请输入上界"))
        V = regtomax(low,high,A[:,i])
    if i == 0:
        X = V.reshape(-1,1) #如果为第一个指标，直接替换x数组
    else:
        X = np.hstack([X,V.reshape(-1,1)])#如果不是第一个指标，水平拼接
print("统一指标类型后的矩阵为：\n",format(X))

#标准化
X = X.astype('float')
for j in range(m):
    X[:,j] = X[:,j]/np.sqrt(np.sum(X[:,j]**2))
print("标准化后的矩阵为：\n",format(X))


#最大最小值的距离
x_max = np.max(X,axis = 0)
x_min = np.min(X,axis = 0)##计算每一列的最大值和最小值
print("最大值为：",format(x_max))
print("最小值为：",format(x_min))
d_z = np.sqrt(np.sum((X-x_max)**2,axis = 1))##和最大值的距离
d_f = np.sqrt(np.sum((X-x_min)**2,axis = 1))##和最小值的距离

s = d_f/(d_z+d_f)##计算得分
score = 100*s/sum(s)
for i in range(len(score)):
    print(f"第{i+1}个评价对象的得分为：{score[i]}")

    
        

    