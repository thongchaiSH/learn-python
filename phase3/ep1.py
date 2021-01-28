# EP1 Exception

# number1=10
# number2=0
# print(number1/number2)

'''
try:
    คำสั่งรันโปรแกรมปกติ
except:
    ที่ทำงานตอนโปรแกรมผิดพลาด
'''

''' Ex1
try:
    number1=10
    number2=0
    print(number1/number2)
except:
    print("Error")
finally:
    print("Finally.")
'''

try:
    number1 = 10
    number2 = 2
    print(number1/number2)  # ZeroDivisionError:
except ValueError:
    print("Error",ValueError)
except ZeroDivisionError:
    print("ห้ามหารด้วย 0",ZeroDivisionError)
except Exception as e:
    print("Error = ",e)
else: #หากรันแล้วไม่มีปัญหา Error จะทำ Else
    print("จบโปรแกรม")
finally:
    print("finally....")
