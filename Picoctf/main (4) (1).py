import base64
str2 = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd"
str3 = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc"
arrayOfByte1 = str2.encode()
arrayOfByte2 = str3.encode()
arrayOfByte3 = []
i = 0
while i < 32:
    a = arrayOfByte2[(arrayOfByte1[i]-90)]
    i = i + 1
    arrayOfByte3.append(a)

letters = ""
for i in arrayOfByte3:
    letters = letters + chr(i)
flag = base64.b64decode(letters).decode("utf-8")
print(flag)