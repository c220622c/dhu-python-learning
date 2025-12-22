from tkinter import *
import random
TIME = 100
def random_fruits(fruit_type)-> int:
    fruit_list = ['香蕉','草莓','苹果','梨子','西瓜','芒果','葡萄']
    fruit_choice_list = {}
    for fruit in fruit_list:
        fruit_choice_list[fruit]=0
    for _ in range(TIME):
        fruit_choice_list[random.choice(fruit_list)]+=1
    return fruit_choice_list[fruit_type]


def main():
    global var, text_output
    root = Tk()
    root.title('水果统计')
    root.geometry('320x240')
    prompt_main = Label(root,text = "请在输入框内输入任意水果名")
    prompt_main.pack()
    var = StringVar()
    fruit_entry = Entry(root,textvariable = var)
    fruit_entry.pack()
    submit_btn = Button(root,text = "提交",command=submit)
    submit_btn.pack()
    text_output = Text(root)
    text_output.pack()
    root.mainloop()
def submit():
    fruit_type = var.get()
    if fruit_type in ['香蕉','草莓','苹果','梨子','西瓜','芒果','葡萄']:
        count = random_fruits(fruit_type)
        s = f"随机{TIME}次,共得到{count}个{fruit_type}\n"
        text_output.insert(END, s)
    else:
        s = f"'{fruit_type}'不在可选水果列表中，请重新输入\n"
        text_output.insert(END, s)
main()
