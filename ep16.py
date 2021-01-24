#Pass เป็นการเขียนให้มันข้ามไปก่อนเหมือนเขียน TDD
age=int(input("Age :"))
if age <= 15:
    if age == 15:
        pass
    elif age == 14:
        pass
    else : 
        print("ประถมศึกษา")
else:
    print("ม.ปลาย")