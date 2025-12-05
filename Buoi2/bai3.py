def Parse(data):
    parts = data.split(",")

    id = parts[0].split("=")[1].strip().replace("'", "")
    size = int(parts[1].split("=")[1].strip())
    fee = int(parts[2].split("=")[1].strip())
    return id, size, fee

class Transaction:
    def __init__(self, id, size, fee, rate):
        self.id = id
        self.size = size
        self.fee = fee
        self.rate = rate

    def __repr__(self):
        return f"- id={self.id}, size={self.size}, fee={self.fee}, rate={self.rate}"

transactions = []
with open("trans3.txt", "r") as f:
    for data in f:
        data = data.strip()
        id, size, fee = Parse(data)
        transaction = Transaction(id, size, fee, fee / size)
        transactions.append(transaction)
    
transactions.sort(key=lambda trans: trans.rate, reverse=True)

total_size = 0
total_fee = 0
arr = []

for trans in transactions:
    if total_size + trans.size <= 1000:
        arr.append(trans)
        total_size += trans.size
        total_fee += trans.fee

print("Danh sách giao dịch được chọn:")
for trans in arr:
    print(trans)

print("\nTổng cỡ:", total_size, "kB")
print("Tổng phí:", total_fee, "satoshi")