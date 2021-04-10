import matplotlib
import numpy as np
from matplotlib import pyplot as plt
# 绘制正弦波
# 计算正弦曲线上点的 x 和 y 坐标
x = np.linspace(-np.pi, np.pi, 256,endpoint=True)
y = np.sin(x)
C,S = np.cos(x), np.sin(x)
plt.title("sine wave form")
# 使用 matplotlib 来绘制点
plt.plot(x, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(x, S, color="red", linewidth=2.5, linestyle="-", label="sine")
#以下是对边界的设置
plt.xlim(x.min()*1.1, x.max()*1.1)
#以下是对x轴的记号设置
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
#以下是对y轴的记号设置
plt.ylim(C.min()*1.1,C.max()*1.1)
plt.yticks([-1, +1],
           [r'$-1$', r'$+1$'])
#以下是对label图例位置进行设置
plt.legend(loc='upper left', frameon=False)
plt.show()