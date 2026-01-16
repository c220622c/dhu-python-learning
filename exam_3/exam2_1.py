import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("图书借阅收费计算程序")
root.geometry("400x300")

# 会员类型和对应的费用信息
member_types = {
    "非会员": {"fee": 0, "price_per_book": 5},
    "白银会员": {"fee": 20, "price_per_book": 2},
    "黄金会员": {"fee": 30, "price_per_book": 1},
    "铂金会员": {"fee": 50, "price_per_book": 0.5}
}

# 存储选中的会员类型
selected_member = tk.StringVar(value="白银会员")

# 标题
title_label = tk.Label(root, text="图书借阅收费计算程序", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# 会员类型选择框架
member_frame = tk.LabelFrame(root, text="选择会员类型", padx=20, pady=10)
member_frame.pack(padx=20, pady=10, fill="x")

# 创建单选按钮
for member_type in member_types.keys():
    rb = tk.Radiobutton(member_frame, text=member_type, variable=selected_member, value=member_type)
    rb.pack(anchor="w")

# 借阅书籍本数输入框架
input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=10, fill="x")

tk.Label(input_frame, text="请输入借阅书籍本数:").pack(anchor="w")
books_entry = tk.Entry(input_frame, width=30)
books_entry.pack(anchor="w", pady=5)

# 计算按钮
def calculate():
    try:
        # 获取输入的书籍本数
        books_num = int(books_entry.get())
        if books_num < 0:
            messagebox.showerror("错误", "借阅书籍本数不能为负数")
            return
        
        # 获取选中的会员类型
        member_type = selected_member.get()
        member_info = member_types[member_type]
        
        # 计算费用
        fee = member_info["fee"]
        price_per_book = member_info["price_per_book"]
        total_cost = fee + books_num * price_per_book
        
        # 显示结果
        result_text = f"会员类型: {member_type}, 借阅书籍本数: {books_num}本, 借阅费用: {total_cost:.2f}元"
        result_label.config(text=result_text)
        
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

calc_button = tk.Button(btn_frame, text="计算", width=15, command=calculate)
calc_button.pack()

# 结果显示标签
result_label = tk.Label(root, text="会员类型: 白银会员, 借阅书籍本数: 50本, 借阅费用: 120.00元", 
                        font=("Arial", 10), wraplength=350)
result_label.pack(pady=20, padx=20)

# 运行程序
root.mainloop()
