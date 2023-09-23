def fx(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        n = int(n)
        return fx(n - 1) + fx(n - 2)

while True:
    value=int(input("请输入项数："))
    print("斐波那契数列\n第{0}项值为{1}".format(value,fx(value)))