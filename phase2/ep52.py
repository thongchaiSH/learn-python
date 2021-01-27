# EP52 Function Return ค่า
'''
1.func ไม่มีการรับและส่งค่า
def name():

2.มีการรับค่าเข้าไปทำงาน
def name(a):

3.รับค่าเข้าไปและส่งกลับ
def add(a,b):
    return
'''

def add(a, b):
    if(a == 0):
        return #บังคับออกจาก function
    else:
        return a+b


ret = add(10, 20)
ret = add(0, 20)
print(ret)
