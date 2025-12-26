from tkinter import *


def main():
    global total, total_var, var1, var2, var3, var4, payment_entry, total_label, payment_label
    root = Tk()
    root.title("自主点餐")
    root.geometry("320x280")
    prompt_main = Label(root, text="你好,请问需要什么")
    prompt_main.pack()

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()

    # 初始化total_var
    total_var = 0

    Checkbutton1 = Checkbutton(
        root, text="汉堡包:12元", variable=var1, onvalue=1, offvalue=0
    )
    Checkbutton1.pack()
    Checkbutton2 = Checkbutton(
        root, text="蛋挞:7元", variable=var2, onvalue=1, offvalue=0
    )
    Checkbutton2.pack()
    Checkbutton3 = Checkbutton(
        root, text="猪肉卷:10元", variable=var3, onvalue=1, offvalue=0
    )
    Checkbutton3.pack()
    Checkbutton4 = Checkbutton(
        root, text="饮料:5元", variable=var4, onvalue=1, offvalue=0
    )
    Checkbutton4.pack()

    submit_btn = Button(root, text="OK", command=submit)
    submit_btn.pack(pady=5)
    # 绑定右键事件
    submit_btn.bind("<Button-2>", lambda _: member_payment())

    # 显示总金额的标签
    total_label = Label(
        root, text="总金额: 0元", font=("Arial", 12, "bold"), fg="black"
    )
    total_label.pack(pady=5)

    payment_frame = Frame(root)
    payment_frame.pack(pady=5)

    payment_input_label = Label(payment_frame, text="付款金额:")
    payment_input_label.pack(side=LEFT)

    payment_entry = Entry(payment_frame, width=10)
    payment_entry.pack(side=LEFT)

    payment_btn = Button(payment_frame, text="付款", command=payment)
    payment_btn.pack(side=LEFT)

    # 显示付款信息的标签
    payment_label = Label(root, text="", font=("Arial", 10), fg="black")
    payment_label.pack(pady=5)

    root.mainloop()


def submit():
    global total
    total = 0
    if var1.get() == 1:
        total += 12
    if var2.get() == 1:
        total += 7
    if var3.get() == 1:
        total += 10
    if var4.get() == 1:
        total += 5
    total_label.config(text=f"总金额: {total}元")


def member_payment():
    """会员付款弹窗"""
    global total

    # 如果总金额为0，提示用户先选择商品
    if total == 0:
        payment_label.config(text="请先选择商品", fg="orange")
        return

    # 创建会员付款弹窗
    member_window = Toplevel()
    member_window.title("会员付款")
    member_window.geometry("300x200")
    member_window.resizable(False, False)

    # 居中显示弹窗
    member_window.transient()
    member_window.grab_set()

    # 会员码输入提示
    prompt_label = Label(member_window, text="请输入会员码:", font=("Arial", 12))
    prompt_label.pack(pady=20)

    # 会员码输入框
    member_entry = Entry(member_window, width=15, font=("Arial", 12))
    member_entry.pack(pady=10)
    member_entry.focus()

    # 显示折扣信息的标签
    discount_label = Label(member_window, text="", font=("Arial", 10), fg="blue")
    discount_label.pack(pady=5)

    # 按钮框架
    button_frame = Frame(member_window)
    button_frame.pack(pady=20)

    def validate_member():
        """验证会员码并计算折扣"""
        global total_var
        member_code = member_entry.get().strip()

        if member_code == "abcdefg":
            # 正确会员码，打8折
            discounted_total = total * 0.8
            discount_label.config(
                text=f"会员验证成功！\n原价: {total}元\n折后价: {discounted_total:.2f}元",
                fg="green",
            )
            # 更新主窗口的总金额显示
            total_label.config(text=f"总金额: {discounted_total:.2f}元 (8折)")
            # 更新total为折后价格
            total_var = discounted_total
        else:
            # 错误会员码，原价
            discount_label.config(
                text=f"会员码错误！\n原价: {total}元\n无折扣", fg="red"
            )
            # 恢复原价显示
            total_label.config(text=f"总金额: {total}元")
            total_var = total

    def confirm_payment():
        global total_var
        # 关闭弹窗
        member_window.destroy()
        # 调用原来的付款逻辑，使用可能打折后的价格
        if total_var != total:
            # 如果有折扣，提示用户输入折后金额
            payment_label.config(
                text=f"会员折扣已应用，请支付{total_var:.2f}元", fg="blue"
            )
        else:
            # 无折扣，正常流程
            payment_label.config(text=f"无会员折扣，请支付{total}元", fg="black")

    # 验证会员码按钮
    validate_btn = Button(button_frame, text="验证", command=validate_member)
    validate_btn.pack(side=LEFT, padx=10)

    # 确认付款按钮
    confirm_btn = Button(button_frame, text="确认付款", command=confirm_payment)
    confirm_btn.pack(side=LEFT, padx=10)

    # 绑定回车键
    member_entry.bind("<Return>", lambda _: validate_member())


def payment():
    global total
    try:
        payment_amount = float(payment_entry.get())
        # 检查是否使用了会员折扣
        current_total_text = total_label.cget("text")
        if "8折" in current_total_text:
            # 提取折后价格
            import re

            match = re.search(r"总金额: ([\d.]+)元", current_total_text)
            if match:
                current_total = float(match.group(1))
            else:
                current_total = total
        else:
            current_total = total

        if payment_amount >= current_total:
            change = payment_amount - current_total
            payment_label.config(
                text=f"收款{payment_amount}元，找零{change:.2f}元", fg="green"
            )
        else:
            payment_label.config(
                text=f"付款金额不足，还需{current_total - payment_amount:.2f}元",
                fg="red",
            )
    except ValueError:
        payment_label.config(text="请输入有效的付款金额", fg="red")


if __name__ == "__main__":
    main()
