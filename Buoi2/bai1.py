import hashlib

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.TinhHash()

    def TinhHash(self):
        block = f"{self.index}{self.data}{self.previous_hash}".encode()
        return hashlib.sha256(block).hexdigest()

class Chain:
    def __init__(self):
        self.chain = []
    def AddBlock(self, data):
        if len(self.chain) == 0:
            new_block = Block(0, data, "0")
        else:
            new_block = Block(
                self.chain[-1].index + 1,
                data,
                self.chain[-1].hash
            )
        self.chain.append(new_block)

    def isOK(self):
        for i, block in enumerate(self.chain):
            if i == 0:
                if block.previous_hash != "0":
                    return False
            else:
                if block.previous_hash != self.chain[i-1].hash:
                    return False
                if block.hash != block.TinhHash():
                    return False
        return True

    def trace(self):
        if self.isOK():
            return
        else:
            for i, block in enumerate(self.chain):
                valid = True
                reasons = []

                if i == 0:
                    if block.previous_hash != "0":
                        valid = False
                        reasons.append("previous_hash != '0'")
                else:
                    if block.previous_hash != self.chain[i-1].hash:
                        valid = False
                        reasons.append("Error previous_hash")

                if block.hash != block.TinhHash():
                    valid = False
                    reasons.append("Error hash")
                print(f"[{block.index}] data={block.data} | prev={block.previous_hash} | hash={block.hash}: {reasons if not valid else 'OK'}")
if __name__ == "__main__":
    chain = Chain()

    chain.AddBlock("Genesis Block")
    chain.AddBlock("An,5,Hoang")
    chain.AddBlock("Hoang,2.5,Duong")
    chain.AddBlock("Duong,1.25,An")

    print("Chain: ", chain.isOK())
    chain.trace()  

    print("--------Dữ liệu sai----------")
    chain.chain[1].data = "An,5000,Hoang" 

    print("Chain: ", chain.isOK())
    chain.trace()            