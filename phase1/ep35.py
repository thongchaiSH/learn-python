#โปรแกรมสร้างขอบตาราง
'''
    3
    ###
    # #
    ###
'''

square=15
for row in range(square):
    for col in range(square):
        if (row>=1 and row<square-1):
            if(col==0 or (col == square-1)): #เส้นขอบแรก และสุดท้าย
                print("x",end='') 
            else :
                print(" ",end='') 
        else:
            print("x",end='') 
    print("")