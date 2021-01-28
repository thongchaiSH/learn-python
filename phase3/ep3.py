# EP3 การสร้าง Exception ด้วย Raise

while True:
    try:
        number1 = int(input("Number1 : "))
        number2 = int(input("Number2 : "))

        if number2 == 0:
            raise Exception("ป้อนค่าตัวหารน้อยกว่า 0") #กำหนด Exception ด้วยตัวเอง

        result = number1/number2
        print("result=", result)
        break
    except Exception as e:
        print("Error", e)
