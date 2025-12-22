import tkinter as tk
from tkinter import ttk
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("用户登录")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # 设置窗口居中
        self.center_window()

        # 正确的用户名和密码
        self.correct_username = "aaa"
        self.correct_password = "aaa"

        self.create_widgets()

    def center_window(self):
        """将窗口居中显示"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        """创建界面组件"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="30")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 配置行列权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # 标题
        title_label = ttk.Label(main_frame, text="用户登录系统", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))

        # 用户名标签和输入框
        username_label = ttk.Label(main_frame, text="用户名:")
        username_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 10))

        self.username_entry = ttk.Entry(main_frame, width=25)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(10, 0))
        self.username_entry.focus()  # 设置初始焦点

        # 密码标签和输入框
        password_label = ttk.Label(main_frame, text="密码:")
        password_label.grid(row=2, column=0, sticky=tk.W, pady=(0, 20))

        self.password_entry = ttk.Entry(main_frame, width=25, show="*")
        self.password_entry.grid(row=2, column=1, pady=(0, 20), padx=(10, 0))

        # 登录按钮
        login_button = ttk.Button(
            main_frame,
            text="登录",
            command=self.login,
            width=20
        )
        login_button.grid(row=3, column=0, columnspan=2, pady=(0, 20))

        # 结果显示标签
        self.result_label = ttk.Label(
            main_frame,
            text="",
            font=("Arial", 12),
            foreground="black"
        )
        self.result_label.grid(row=4, column=0, columnspan=2, pady=(0, 10))

        # 绑定回车键
        self.root.bind('<Return>', lambda event: self.login())
        self.password_entry.bind('<Return>', lambda event: self.login())

    def login(self):
        """处理登录逻辑"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            self.show_result("请输入用户名和密码！", "red")
            return

        if username == self.correct_username and password == self.correct_password:
            self.show_result(f"登录成功！欢迎您，{username}！", "green")
            # 清空输入框
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.username_entry.focus()
        else:
            self.show_result("用户名或密码错误，请重试！", "red")
            # 清空密码框，保持用户名
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus()

    def show_result(self, message, color):
        """显示结果信息"""
        self.result_label.config(text=message, foreground=color)

        # 3秒后清除成功消息
        if "成功" in message:
            self.root.after(3000, lambda: self.result_label.config(text=""))

def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
