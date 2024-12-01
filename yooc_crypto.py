import base64
import binascii
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decrypt(cipher, yibanId):
    cipher = base64.b64decode(cipher).hex()

    salt = 'yooc@admin'
    iv = '42e07d2f7199c35d'.encode('utf-8')
    md5 = hashlib.md5()
    md5.update((salt + yibanId).encode('utf-8'))
    key = str(md5.hexdigest()[8:24]).encode('utf-8')
    
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    
    encrypted_data = binascii.unhexlify(cipher)
    decrypted_data = unpad(aes.decrypt(encrypted_data), AES.block_size)
    return decrypted_data.decode('utf-8').encode('utf-8').decode('unicode_escape')

def encrypt(plain, yibanId):
    plain = plain.encode('unicode_escape').decode('utf-8')

    salt = 'yooc@admin'
    iv = "42e07d2f7199c35d".encode("utf-8")
    md5 = hashlib.md5()
    md5.update((salt + yibanId).encode("utf-8"))
    key = str(md5.hexdigest()[8:24]).encode("utf-8")

    aes = AES.new(key, AES.MODE_CBC, iv=iv)

    padded_data = pad(plain.encode('utf-8'), AES.block_size)
    encrypted_data = aes.encrypt(padded_data)
    return base64.b64encode(encrypted_data).decode("utf-8")

def encrypt_score(score, yibanId):
    plain = 'yooc@admin' + str(score)
    return encrypt(plain, yibanId)