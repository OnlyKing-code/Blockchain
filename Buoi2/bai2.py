def Parse(data):
    parts = data.split(",")

    from_wallet = parts[0].split("=")[1].strip().replace("'", "")
    to_wallet = parts[1].split("=")[1].strip().replace("'", "")
    ammout = int(parts[2].split("=")[1].strip())
    return from_wallet, to_wallet, ammout

wallets = {}
with open("trans.txt", "r") as f:
    for data in f:
        data = data.strip()
        from_wallet, to_wallet, ammout = Parse(data)
        if from_wallet not in wallets:
            wallets[from_wallet] = 0
        if to_wallet not in wallets:
            wallets[to_wallet] = 0
        wallets[from_wallet] -= ammout
        wallets[to_wallet] += ammout
print("Số dư các ví sau các giao dịch:")
for wallet, balance in wallets.items():
    print(f"{wallet}: {balance}")