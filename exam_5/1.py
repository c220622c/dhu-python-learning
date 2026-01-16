import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("酒店客房预订费用计算系统")
root.geometry("350x300")

# 房型价格
rooms = {"标准间": 280, "豪华大床房": 450, "行政套房": 880}
selected_room = tk.StringVar(value="标准间")

# 服务费
breakfast_var = tk.BooleanVar(value=False)
extra_bed_var = tk.BooleanVar(value=False)

# 房型选择
room_frame = tk.LabelFrame(root, text="房型", padx=10, pady=5)
room_frame.pack(padx=10, pady=5, fill="x")
for room in rooms:
    tk.Radiobutton(room_frame, text=room, variable=selected_room, value=room).pack(anchor="w")

# 服务选择
service_frame = tk.LabelFrame(root, text="服务", padx=10, pady=5)
service_frame.pack(padx=10, pady=5, fill="x")
tk.Checkbutton(service_frame, text="含双早", variable=breakfast_var).pack(anchor="w")
tk.Checkbutton(service_frame, text="加床服务", variable=extra_bed_var).pack(anchor="w")

# 入住天数
tk.Label(root, text="入住天数:").pack(anchor="w", padx=10, pady=(10, 0))
days_entry = tk.Entry(root, width=30)
days_entry.pack(padx=10, pady=2)

# 计算函数
def calculate():
    try:
        days = int(days_entry.get())
        if days <= 0:
            messagebox.showerror("错误", "入住天数必须为正整数")
            return
        
        room = selected_room.get()
        price = rooms[room]
        fee = (60 if breakfast_var.get() else 0) + (150 if extra_bed_var.get() else 0)
        total = (price + fee) * days
        
        result_text = f"房型: {room}\n入住天数: {days}晚\n应付总金额: {total}元"
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("错误", "请输入有效数字")

# 计算按钮
tk.Button(root, text="计算", command=calculate).pack(pady=10)

# 结果显示
result_label = tk.Label(root, text="房型: 标准间\n入住天数: 2晚\n应付总金额: 560元", 
                        font=("Arial", 10), justify="left", relief="sunken", padx=10, pady=10)
result_label.pack(pady=10, padx=10, fill="both", expand=True)

root.mainloop()
