
sum,avg,round=0,0,0;
while True:
    number=int(input("Input Number ="))
    sum+=number
    round+=1
    if sum>100:
        break

avg=sum/round

print("ผลรวม = ",sum)
print("ค่าเฉลี่ย = ",avg)