#หาเลขยกกำลัง
number=[1,2,3,4,5,6,7]

#ปกติ
# for i in range(len(number)):
#     number[i]=number[i]**2
#     print(i,"=",number[i])


#ลบรูป
# [print(i*i) for i in number]
number=[i*i for i in number]
print(number)