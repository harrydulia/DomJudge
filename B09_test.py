def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

# 输入四个值
a, b, c, d = map(int, input("请输入四个值，用空格分隔：").split())

# 计算四个值的总和
total_sum = a + b + c + d

# 计算四个值的斐波那契数总和
fibonacci_sum = fibonacci(a) + fibonacci(b) + fibonacci(c) + fibonacci(d)

# 输出结果
print("四个值的总和为：", total_sum)
print("四个值的斐波那契数总和为：", fibonacci_sum)
