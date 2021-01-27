# list, tuple
lis =["แดง","เหลือง","เขียว"]
tup = ("แดง","เหลือง","เขียว")

print(lis)
print(tup)

#dictionary => key,value
colors={"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว"}
students={"กล้อง":40,"โจ้":50,"โคช":100}
print(colors['red'],colors)
print(students)

animals=dict(cat="แมว",dog="หมา",duck="เป็ด")
print(animals['cat'])
print(animals.get('cat'))
animals['cat']="น้อยแมว"

animals.update({"ox":"วัว"})
print(animals)
colors.update({"red":"แดง","pink":"ชมพู"})

#Loop
for item  in colors:
    print(item) #Key

for item  in colors.values(): #Key
    print(item)

for item  in colors.keys():  #Value
    print(item)

for k,v in colors.items():
    print("Key=",k,"Value=",v)

#การลบ
print(colors)
colors.pop('yellow')
print(colors)
colors.popitem(); #ลบข้อมูลล่าสุด
print(colors)
# colors.clear(); #ลบข้อมูล
# print(colors)
# del colors

#การ copy
x=colors.copy()
print(x)

#Nested dictionary การซ้อน dic
market={
    "ร้านป้าพร":{
       "type":"ขายอาหารตามสั่ง",
       "zone":"A",
       "menu":["กระเพราไก่","ก๊วยเตี๋ยว"]
    },
    "ร้านลุงป้อม":{
        "type:":"ขายผลไม้",
        "zone":"C"
    }
}
print(market)
print(market['ร้านป้าพร']['menu'])

if "ก๊วยเตี๋ยว" in market['ร้านป้าพร']['menu']:
    print("ร้านป้าพรมีก๊วยเตี๋ยว")