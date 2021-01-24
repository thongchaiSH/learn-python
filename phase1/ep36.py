#โปรแกรมทายลูกเต๋า
# 1,2,3,4,5,6
import random

myrand=random.randrange(1,7) #1-6
print(myrand)
correct=False
while correct==False:
    number=int(input("ป้อนคำตอบของคุณ = "))
    if number==myrand:
        print("Correct !!")
        correct=True
    else :
        print("Incorrect !!")
    # Hint
    if myrand<number:
        print("น้อยกว่า")
    elif myrand>number:
        print("มากกว่า")