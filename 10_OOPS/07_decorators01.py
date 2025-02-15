def debugg(func):
    def wrapper(*args,**kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} = {v}" for k,v in kwargs.items())
        print(f"calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    
    return wrapper



# def hello():
#     print("hello")

@debugg
def greet(name,greeeting="hello"):
    print(f"{greeeting},{name}");
greet("chai",greeeting="han ji")