import os


__all__ = [
    "add",  # 这个符号对应的对象现在还没有真正被加载
    "sub"  # 这个符号对应的对象现在还没有真正被加载
]


def print_in_box(message):
    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    border = '#' * (max_length + 4)
    
    print(border)
    for line in lines:
        print(f"# {line.ljust(max_length)} #")
    print(border)


print()
print_in_box("rainbow初始化开始...")

################################################################################
# Load dll
################################################################################
dll_path = os.path.join(os.path.dirname(__file__), "lib")
os.add_dll_directory(dll_path)                                                                      
                                                                                            
from rainbow.math import add, sub  # 这里指定rainbow.math就是导入了pyd，而不是math目录；要导入math目录就是.math
print_in_box(f"成功添加扩展包的动态库路径, dll_path:\ndll_path)")
################################################################################

print_in_box("rainbow初始化完毕.")

del print_in_box, dll_path
print()