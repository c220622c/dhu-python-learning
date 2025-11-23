import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import openpyxl
from openpyxl.chart import BarChart, Reference

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_table(
    "/Users/wzj/Documents/Coding-repo/dhu-python/230250329_8/newscore.txt",
    sep=",",
    names=["学号", "名字", "班级", "成绩"],
)

# 计算每个班级的平均分
class_avg = df.groupby("班级")["成绩"].mean().reset_index()
class_avg.columns = ["班级", "平均分"]
class_avg = class_avg.sort_values("平均分", ascending=False)

# 将原始数据和班级均分保存到Excel
excel_path = "/Users/wzj/Documents/Coding-repo/dhu-python/230250329_8/data.xlsx"
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    # 保存原始数据
    df.to_excel(writer, sheet_name='原始数据', index=False)
    # 保存班级均分
    class_avg.to_excel(writer, sheet_name='班级均分', index=False)

# 读取Excel文件以添加图表
wb = openpyxl.load_workbook(excel_path)
ws_class = wb['班级均分']

# 创建图表
chart = BarChart()
chart.type = "col"
chart.style = 10
chart.title = "班级平均分统计图"
chart.y_axis.title = '平均分'
chart.x_axis.title = '班级'
chart.legend = None

# 设置数据范围
data = Reference(ws_class, min_col=2, min_row=1, max_row=len(class_avg) + 1)
categories = Reference(ws_class, min_col=1, min_row=2, max_row=len(class_avg) + 1)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

# 将图表插入到工作表中
ws_class.add_chart(chart, "D2")

# 保存Excel文件
wb.save(excel_path)

print("班级均分计算完成！")
print("\n班级均分统计：")
print(class_avg.to_string(index=False))
print(f"\n结果已保存到: {excel_path}")
