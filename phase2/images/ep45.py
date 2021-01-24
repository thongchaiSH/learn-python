# การค้นหาและนับจำนวนตัวอักษร
message = ["aa", "bb", "cba", "asd", "cba"]
# for msg in message:
#     print(msg)
#     for i in msg:
#         print(i,"=",msg.count(i))

# ลบรูป
[print(i, "=", msg.count(i)) for msg in message for i in msg]
