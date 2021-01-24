#โครงสร้างควบคุมแบบทำซ้ำ

#while expression
'''
while expression:
    statement
'''
i=0
while i<3:
    print("Hello world")
    i+=1

#ผลรวมของตัวเลข 1+2+3+4..
i=1
summation=0;
average=0;
while i<=10:
    summation+=i
    i+=1

average=summation/i;
print("result",summation)
print("average",average)


# For
#for in range(start,stop,step) #กำหนดรอบ
for i in range(3):
    print("Hello world round : ",i)

for i in range(0,6,2):
    print("Hello world round : ",i)

for i in range(10,0,-1):
    print("Count down",i)