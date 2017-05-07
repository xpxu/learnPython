
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

num = int(raw_input('please input your num> '))
print factorial(num)

