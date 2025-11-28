import hashlib

def hash256(filename):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        data = f.read()
        sha256.update(data)
    return sha256.hexdigest()

filename = "test.txt"  
print("Chuỗi đã mã hóa: " + hash256(filename))
