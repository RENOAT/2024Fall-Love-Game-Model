import nashpy as nash
import numpy as np

p = 1
q = 1
m = 3
n = 3
x = 0
y = 0

A_p = np.array([[m, -q], [x, x]])  # 局中人1的赢得矩阵
B_p = np.array([[n, -p], [y, y]])   # 局中人2的赢得矩阵

# 创建博弈模型
game = nash.Game(A_p, B_p)      

# 求解纳什均衡
equilibria= list(game.support_enumeration())

# 输出结果
print("纳什均衡解:")
for eq in equilibria:
    print(eq)

