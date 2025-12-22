from tkinter import *


def main():
    global total, var1, var2, var3, var4, payment_entry, total_label, payment_label
    root = Tk()
    root.title("自主点餐")
    root.geometry("320x280")
    prompt_main = Label(root, text="你好,请问需要什么")
    prompt_main.pack()

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()

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


def payment():
    global total
    try:
        payment_amount = float(payment_entry.get())
        if payment_amount >= total:
            change = payment_amount - total
            payment_label.config(
                text=f"收款{payment_amount}元，找零{change}元", fg="green"
            )
        else:
            payment_label.config(
                text=f"付款金额不足，还需{total - payment_amount}元", fg="red"
            )
    except ValueError:
        payment_label.config(text="请输入有效的付款金额", fg="red")


if __name__ == "__main__":
    main()
