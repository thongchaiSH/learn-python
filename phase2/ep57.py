#EP57 Fibonacci number


def fibonacci(number):
    if number<=1:
        return number #2 ลำดับแรก
    else :
        return fibonacci(number-1)+fibonacci(number-2) #เลขลำดับถัดไป


for i in range(5):
    print(fibonacci(i))