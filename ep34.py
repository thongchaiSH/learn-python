#โปรแกรมสร้างตารางหมากฮอต
square=8
for row in range(square):
    for col in range(square):
        # if  col%2==0:
        #     if row%2==0:
        #         print("o",end='') 
        #     else:
        #         print("x",end='') 
        # else :
        #     if row%2==0:
        #         print("x",end='') 
        #     else:
        #         print("o",end='') 
        # Solution 2
        # if (row+col)%2==0:
        #     print("x",end='') 
        # else :
        #     print("o",end='') 
        # Solution 3
        print("x",end='') if (row+col)%2==0 else print("o",end='') 
           
    print("") #new line