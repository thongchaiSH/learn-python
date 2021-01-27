def addOne(x,y):
    print(x+y)

def sumThree(a,b,c):
    print(a+b+c)

def sumFour(a,b,c,d):
    print(a+b+c,d)

# *agrs
def add(*agrs):
    print(agrs)
    sum=0
    for item in agrs:
        sum+=item
    print("sum = ",sum)

def minus(*num):
    sum=0
    for item in num:
        sum-=item
    print("minus = ",sum)

add(10,20,4,5)
sumThree(1,2,3)
sumFour(1,2,3,4)
minus(2,3,4,5)