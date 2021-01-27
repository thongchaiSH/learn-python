#EP54 Function เรียก Function
def equal(x,y,z):
    max=compareMax(x,y)
    max=compareMax(max,z)
    return max;

def equalShort(x,y,z):
    return compareMax(compareMax(x,y),z)

def compareMax(x,y):
    if x>y:
        return x
    else:
        return  y

print(compareMax(1,2))
max=equal(11,2,23)
print("Max = ",max)
print("Max Short = ",equalShort(1,2,3))