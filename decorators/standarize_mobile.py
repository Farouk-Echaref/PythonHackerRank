#!/usr/bin/python3

# first ex
# def outer():
#     x = 1
#     y = 1
#     def inner():
#         nonlocal x 
#         print ("inner x: ",x)
#         x = 2
#         y = 2
#         print ("inner y: ",y)
#     inner()
#     print ("outer x: ",x)
#     print ("outer y: ",y)

# outer()

# second ex
# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def apply(func, x, y):
#     return func(x, y)

# print(apply(add,2, 1))
# print(apply(sub,2, 1))

# third ex
# def outer():
#     x = 1
#     def inner():
#         print (x)
#     return inner
# foo = outer()
# print(foo.func_closure)

# fourth ex
# def outer(func):
#     def inner():
#         res = func()
#         return res + 1
#     return inner

# def foo():
    # return 1

# decorated = outer(foo)
# print(decorated())


# @outer
# def foo():
#     return 1
# print(foo())


def my_format(num: str):
    return f"{num[:3]} {num[3:8]} {num[8:]}"

def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            num = l[i]
            if len(num) == 10:
                l[i] = "+91" + num
            elif num.startswith('0'):
                l[i] = num.replace('0', "+91", 1)
            elif not num.startswith('+'):
                l[i] = "+" + num
        for i in range(len(l)):
            l[i] = my_format(l[i])
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


