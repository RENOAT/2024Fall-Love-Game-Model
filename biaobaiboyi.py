import nashpy as nash
import numpy as np

# 定义赢得矩阵
# 对于追求者，赢得矩阵中的行表示其策略：[表白，不表白]
# 对于被追求者，赢得矩阵中的列表示其策略：[接受表白，不接受表白]

a = 4
b = 4
c = 2
d = 3

# 被追求者满意的情况
A_p = np.array([[a, -c], [0, 0]])  # 追求者的赢得矩阵
B_p = np.array([[b, 0], [0, 0]])   # 被追求者的赢得矩阵

# 被追求者不满意的情况
A_1_p = np.array([[a, -c], [0, 0]])  # 追求者的赢得矩阵
B_1_p = np.array([[-d, 0], [0, 0]])  # 被追求者的赢得矩阵

# 创建博弈模型
game_satisfied = nash.Game(A_p, B_p)      # 被追求者满意
game_not_satisfied = nash.Game(A_1_p, B_1_p)  # 被追求者不满意

# 求解纳什均衡
equilibria_satisfied = list(game_satisfied.support_enumeration())
equilibria_not_satisfied = list(game_not_satisfied.support_enumeration())

# 输出结果
print("被追求者满意的情况下的纳什均衡:")
for eq in equilibria_satisfied:
    print(eq)

print("\n被追求者不满意的情况下的纳什均衡:")
for eq in equilibria_not_satisfied:
    print(eq)
