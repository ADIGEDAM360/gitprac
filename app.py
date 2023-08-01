def outer(func):
    def inner():
        print("inside the inner functuion")
        func()
        print("parameterized function exceuted")
    return inner()
def outer2(func):
    def inner2():
        print("inside the inner functuion")
        func()
        print("parameterized function exceuted")
    return inner2()

@outer
def trail(a, b ):
    c = a+b
    return c
 

def  multiplication (a,b):
    return a*b