def sum(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)
print(sum(1,2,3))