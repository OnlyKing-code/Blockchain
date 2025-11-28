import hashlib
from importlib.metadata import files
import os

def hash256(filename):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        data = f.read()
        sha256.update(data)
    return sha256.hexdigest()

def main():
    files = input("Nhập danh sách file: ").strip()
    if files == "":
        folder = "d:\\Duy Hoàng học đại học\\Năm ba\\Blockchain"

        for filename in os.listdir(folder):
            path = os.path.join(folder, filename)
            if os.path.isfile(path):
                print(f"{filename}: {hash256(path)}")
    files = files.split()
    for i in files:
        print(f"{i}: {hash256(i)}")

if __name__ == "__main__":
    main()
    