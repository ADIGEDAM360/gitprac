def outer(func):
    def inner():
        print("inside the inner functuion")
        func()
        print("parameterized function exceuted")
    return inner()
def outer(func):
    def inner():
        print("inside the inner functuion")
        func()
        print("parameterized function exceuted")
    return inner()
 
 