# 关于函数与列表的参数联动
import importlib.util

# 导入模块
spec = importlib.util.spec_from_file_location("module9_3", "230250329_9_3.py")
module9_3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module9_3)


def sth():
    print("This is a placeholder function.")
