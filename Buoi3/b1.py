import hashlib

BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def base58_encode(raw_bytes):
    n = int.from_bytes(raw_bytes, byteorder='big')
    result = ""
    while n > 0:
        n, remainder = divmod(n, 58)
        result = BASE58_ALPHABET[remainder] + result
    for byte in raw_bytes:
        if byte == 0:
            result = BASE58_ALPHABET[0] + result
        else:
            break
    return result

def WalletsAdress(public_key_hex):
    print(f"Public Key: {public_key_hex}")
    public_key_bytes = bytes.fromhex(public_key_hex)
    #Bước 1
    sha256_1 = hashlib.sha256(public_key_bytes).digest()
    #Bước 2
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_1)
    hashed_public_key = ripemd160.digest()
    #Bước 3
    version_byte = b'\x00'
    ver_hashed_pubkey = version_byte + hashed_public_key
    #Bước 4
    first_sha = hashlib.sha256(ver_hashed_pubkey).digest()
    second_sha = hashlib.sha256(first_sha).digest()
    checksum = second_sha[:4]
    #Bước 5
    final_payload = ver_hashed_pubkey + checksum
    #Bước 6
    address = base58_encode(final_payload)  
    return address

publickey = "0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352"
final_address = WalletsAdress(publickey)
print(f"\nĐịa chỉ ví hoàn chỉnh: {final_address}")