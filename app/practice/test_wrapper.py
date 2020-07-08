from functools import wraps

# 定义装饰器
def extend(fuc):
    @wraps(fuc)
    def hello(*args, **kwargs):
        print("hello")
        print(args)
        print(kwargs)
        fuc(*args, **kwargs)
        print("Good bye!")
    return hello


@extend
def tmp(a:int, b:str, c, d)->int:
    print("tmp")

@extend
def tmp1():
    print("tmp1")

def test_wrapper():
    tmp(1,"2",3,d=10)
    print(tmp.__annotations__)
    tmp1()


