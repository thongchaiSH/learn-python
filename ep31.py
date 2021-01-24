#โปรแกรมหาค่าตัวเลขมากสุด น้อยสุด
max,min=0,0
while True:
    number=int(input("Input number : "))
    if number==0:
        break
    
    if number>max:
        max=number
    if number<min:
        min=number
    print("Max =",max,"Min =",min)