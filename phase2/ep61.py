# EP61 นับตัวอักษรพิมใหญ่/เล็ก

def checkStr(message):
    result = {"UPPER": 0, "LOWER": 0}
    for char in message:
        print(char)
        if char.isupper():
            result['UPPER'] += 1
        elif char.islower():
            result['LOWER'] += 1
    return result


print(checkStr("AbcEds"))
