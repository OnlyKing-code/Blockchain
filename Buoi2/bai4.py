import hashlib

data = "Hoang 5 Duong"
n = int(input("N = "))

target = "0" * n
nonce = 0
trials = 0

while True:
    trials += 1
    text = data + str(nonce)
    hash = hashlib.sha256(text.encode()).hexdigest()
    if hash.startswith(target):
        print(f"Nonce tìm được: {nonce}")
        print(f"Hash tương ứng: {hash}")
        print(f"Số lần thử: {trials}")
        break
    nonce += 1