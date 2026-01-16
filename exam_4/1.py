import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("游乐园售票系统")
root.geometry("400x350")

# 票价信息
ticket_prices = {
    "成人票": 100,
    "学生票": 50,
    "儿童票": 30
}

# 快速通道费用
vip_fee = 40

# 存储选中的票类型
selected_ticket = tk.StringVar(value="成人票")

# 存储VIP状态
vip_var = tk.BooleanVar(value=False)

# 标题
title_label = tk.Label(root, text="游乐园售票系统", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# 票类型选择框架
ticket_frame = tk.LabelFrame(root, text="选择票类型", padx=20, pady=10)
ticket_frame.pack(padx=20, pady=10, fill="x")

# 创建单选按钮
for ticket_type in ticket_prices.keys():
    rb = tk.Radiobutton(ticket_frame, text=ticket_type, variable=selected_ticket, value=ticket_type)
    rb.pack(anchor="w")

# VIP快速通道复选框
vip_frame = tk.Frame(root)
vip_frame.pack(padx=20, pady=10, fill="x")

vip_cb = tk.Checkbutton(vip_frame, text="快速通道(+40元/张)", variable=vip_var)
vip_cb.pack(anchor="w")

# 购票数量输入框架
input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=10, fill="x")

tk.Label(input_frame, text="购票数量:").pack(anchor="w")
quantity_entry = tk.Entry(input_frame, width=30)
quantity_entry.pack(anchor="w", pady=5)

# 计算按钮
def calculate():
    try:
        # 获取输入的购票数量
        quantity = int(quantity_entry.get())
        if quantity <= 0:
            messagebox.showerror("错误", "购票数量必须为正整数")
            return
        
        # 获取选中的票类型
        ticket_type = selected_ticket.get()
        base_price = ticket_prices[ticket_type]
        
        # 计算单张票价
        unit_price = base_price
        if vip_var.get():
            unit_price += vip_fee
        
        # 计算总费用
        total_cost = unit_price * quantity
        
        # 显示结果
        result_text = f"类型: {ticket_type}\n数量: {quantity}张\n总费用: {total_cost}元"
        result_label.config(text=result_text)
        
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

calc_button = tk.Button(btn_frame, text="计算费用", width=15, command=calculate)
calc_button.pack()

# 结果显示标签
result_label = tk.Label(root, text="类型: 成人票\n数量: 3张\n总费用: 300元", 
                        font=("Arial", 11), justify="left", relief="sunken", padx=10, pady=10)
result_label.pack(pady=15, padx=20, fill="both")

# 运行程序
root.mainloop()