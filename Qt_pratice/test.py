# num = ""
def fun1():
    global num  # 需要使用 global 关键字声明
    # print(num)
    num = 123
    # print(num)
fun1()
print(num)