#จับคู่คำทักทาย / บุคคล
'''
็Hi,Hello
กล้อง,แก้ม
'''
gretiing=["สวัสดี","Hi !!","Hello","Good bye"]
people=["กล้อง","แก้ม","โจ้"]
result=[]
# แบบปกติ
for x in gretiing:
    for y in people:
        result.append(x+y)

print("result",result)

#แบบลดรูป
result.clear()
result=[x+y for x in gretiing for y in people ]
print("result",result)