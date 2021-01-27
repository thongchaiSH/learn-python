# EP55 Recursive Function
'''
1-> หาจุดวนซ้ำ
2-> หาจุดออกจาก Function (return)
ต้องมี parameter
'''


def display(num):
    if num == 5:  # จุดออก
        return
    print(num)
    num += 1
    display(num)  # หาจุดวนซ้ำ


def summation(number):
    print(number)
    if number == 1:
        return number
    else:
        return number+summation(number-1)


'''
5
5 + summation(5-1)
5 + 4 + summation(3)
5 + 4 + 3 + summation(2)
5 + 4 + 3 + 2+ summation(1)
5 + 4 + 3 + 2+ 1
'''

ret = summation(5)  # 5+4+3+2+1
print(ret)
# display(0)
