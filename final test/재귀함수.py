def hello(count):
    if count ==0:
        return
    

    print('hello,world',count)


    count-= 1
    hello(count)


def factorial(n):
    if n == 1:
        return 1
    return n *factorial(n-1)
print(factorial(5))
