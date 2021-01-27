# EP63 หอคอยฮานอย
'''
n= จำนวนจาน
เสา => A,B,C
มีจาน 3 จาน
n =1 
n =2
n =3 (ใหญ่สุด)
'''

def hanoi(n,a,b,c):
    # a => C
    if n ==0:
        return
    hanoi(n-1,a,c,b) #ย้าย a (ล,ก) ->b | c จุดพัก
    print("Disk =",n,"From =",a,"To =",c)
    hanoi(n-1,b,a,c)

hanoi(3,"A","B","C")