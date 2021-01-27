#- EP62 หาเบอร์โทรที่กำหนด

data={
    "191":"แจ้งเหตุด่วน",
    "1668":"เบอร์โรงพยาบาล"
}

def searchNumber(message):
    for key,value in data.items():
        print("key",key)
        print("value",value)
        if value==message:
            return key

print(searchNumber("แจ้งเหตุด่วน"))