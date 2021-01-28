# EP4 การสร้างโปรแกรมบัญชีธนาคาร

# data
account = {"นายA": 5000, "นายB": 1000}


def getBalance():
    print("ยอดเงินคงเหลือในบัญชี", account)


def deposit(money):
    if money <= 0:
        raise Exception("จำนวนเงินไม่ถูกต้อง")

    print("ฝากเงินเข้าบัญชี", money)
    account['นายA'] += money


def withdraw(money):
    if money <= 0:
        raise Exception("จำนวนเงินไม่ถูกต้อง")
    if money > account['นายA']:
        raise Exception("จำนวนเงินไม่พอสำหรับถอน")

    print("ถอนเงินเข้าบัญชี", money)
    account['นายA'] -= money


def transfer(money):
    if not (type(money) is int  or type(money) is float):
        raise Exception("รูปแบบจำนวนเงินไม่ถูกต้อง")

    if money <= 0:
        raise Exception("จำนวนเงินไม่ถูกต้อง")
    if money > account['นายA']:
        raise Exception("จำนวนเงินไม่พอสำหรับถอน")

    print("โอนเงินไป B", money)
    account['นายA'] -= money
    account['นายB'] += money


try:
    transfer(1)
    # getBalance()
    # deposit(1000)
    # getBalance()
    # withdraw(10000)
    # getBalance()
    # transfer(3000)
    # getBalance()
except Exception as e:
    print("Error =", e)
