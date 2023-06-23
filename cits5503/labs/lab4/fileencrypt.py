import os, random, struct, boto3, base64, hashlib
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16
CHUNK_SIZE = 64 * 1024

def encrypt_file(password, in_filename, out_filename):
    key = hashlib.sha256(password.encode("utf-8")).digest()
    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' '.encode("utf-8") * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(password, in_filename, out_filename):
    key = hashlib.sha256(password.encode("utf-8")).digest()
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)

password = 'kitty and the kat'

encrypt_file(password,"kms.txt", out_filename="kms.txt.enc")
decrypt_file(password, "kms.txt.enc", out_filename="kms.txt.dec")
with open('kms.txt.enc', 'rb') as file:
    boto3.client("s3").upload_fileobj(file, '22792191-cloudstorage', "kms.txt.enc")