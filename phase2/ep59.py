# EP59 lamda function

def getCity(name):
    print(name)


def myPower(x):
    # x=ตัวเลข
    # a=เลขชี้กำลัง
    return lambda a: x**a


'''
lamda arguments : expression จะ return auto
'''
def x(name): return name


def sum(x, y): return x+y
def multiply(a, b): return a*b


print(x("thongchai"))
print(sum(1, 2))
print(multiply(2, 3))
y=myPower(5)
result=y(2)
print(result)
