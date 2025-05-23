#!/usr/bin/env python3
# 简单的Python示例程序

# 列表操作
numbers = [1, 2, 3, 4, 5]
print("列表:", numbers)
print("列表求和:", sum(numbers))
print("列表平均值:", sum(numbers) / len(numbers))

# 字典操作
person = {
    "name": "Zhang San",
    "age": 30,
    "city": "Beijing"
}
print("\n字典:", person)
print("姓名:", person["name"])

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print("\n平方数:", squares)

# 函数定义
def greet(name):
    return f"你好, {name}!"

print("\n" + greet("世界"))

# 类定义
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

calc = Calculator()
print("\n计算器:")
print("3 + 4 =", calc.add(3, 4))
print("10 - 5 =", calc.subtract(10, 5)) 