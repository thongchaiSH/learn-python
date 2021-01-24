#โปรแกรมการหาผลรวมและค่าเฉลี่ย
#start=int(input("Start = "))
#stop=int(input("Stop = "))
start,stop = 1,5
sum=0;
avg=0;
for i in range(start,stop+1):
    number=int(input("Input Number ="))
    sum+=number
avg=sum/stop

print("ผลรวม = ",sum)
print("ค่าเฉลี่ย = ",avg)