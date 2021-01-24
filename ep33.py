#โปรแกรมสร้างภาพวาด 4 เหลี่ยมจตุรัส
'''
input 3
xxx
xxx
xxx
inpuit 2
xx
xx
'''
square=int(input("Size ="))
for row in range(square):
    for col in range(square):
        print("x",end='') 
    print("") #new line