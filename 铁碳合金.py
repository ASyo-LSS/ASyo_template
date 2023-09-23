# -*- codeing = utf-8 -*-
# Author：ASyo
# Date：2023-9-6
# Time：23:55
import pandas as pd
import matplotlib.pyplot as plt

# 读取铁碳合金相图数据
data = pd.read_csv('Fe_C_phase_diagram.csv')

# 提取温度、碳含量和相信息
temperature = data['Temperature']
carbon_content = data['Carbon_Content']
phase = data['Phase']

# 创建一个空的相图
plt.figure(figsize=(10, 6))

# 绘制不同相的散点图
for phase_name in set(phase):
    phase_data = data[data['Phase'] == phase_name]
    plt.scatter(phase_data['Carbon_Content'], phase_data['Temperature'], label=phase_name)

# 添加标签和标题
plt.xlabel('Carbon Content (wt %)')
plt.ylabel('Temperature (°C)')
plt.title('Iron-Carbon Alloy Phase Diagram')

# 添加图例
plt.legend()

# 显示图形
plt.grid(True)
plt.show()
