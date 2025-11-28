a = input("Nhập chế độ: ")
b = int(input("Nhập khóa: "))
c = input("text: ")

text = c.encode()
result = []
for i in text:
    result.append(i ^ b)
if a == 'e':
    print("Mã hóa: " + bytes(result).decode())
elif a == 'd':
    print("Giải mã: " + bytes(result).decode())

    