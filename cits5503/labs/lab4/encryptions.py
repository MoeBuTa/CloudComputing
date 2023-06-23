import boto3
import base64
from cryptography.fernet import Fernet

client = boto3.client("kms")
s3 = boto3.client("s3")
KEY_ID = '626af620-50ae-41e9-8f51-74a1bec20f64'
KEY_SPEC = 'AES_256'
FILENAME = 'kms.txt'
BUCKET = '22792191-cloudstorage'
NUM_BYTES_FOR_LEN = 4

def create_data_key():
    response = client.generate_data_key(KeyId=KEY_ID, KeySpec=KEY_SPEC)
    data_key_encrypted = response['CiphertextBlob']
    data_key_plaintext = base64.b64encode(response['Plaintext'])
    print('Encrypted data key: '+ str(data_key_encrypted))
    print('Plaintext data key: '+ str(data_key_plaintext))
    return data_key_encrypted, data_key_plaintext

def encrypt_file():
    data_key_encrypted, data_key_plaintext = create_data_key()
    # encrypt a local file
    with open(FILENAME, 'rb') as file:
                file_contents = file.read()
    f = Fernet(data_key_plaintext)
    file_contents_encrypted = f.encrypt(file_contents)
    with open(FILENAME + '.encrypted', 'wb') as file_encrypted:
        file_encrypted.write(len(data_key_encrypted).to_bytes(NUM_BYTES_FOR_LEN,
                                                                byteorder='big'))
        file_encrypted.write(data_key_encrypted)
        file_encrypted.write(file_contents_encrypted)
    # upload encrypted file to s3 bucket
    with open(FILENAME, 'rb') as file:
        s3.upload_fileobj(file, BUCKET, FILENAME + '.encrypted', 
                          ExtraArgs={'ServerSideEncryption': "aws:kms", "SSEKMSKeyId":KEY_ID})

def decrypt_data_key(data_key_encrypted):
    # Decrypt the data key
    kms_client = boto3.client('kms')
    response = kms_client.decrypt(CiphertextBlob=data_key_encrypted)
    return base64.b64encode((response['Plaintext']))


def decrypt_file():
    # download file from cloud
    s3.download_file(BUCKET, FILENAME,  FILENAME)
    with open(FILENAME + '.encrypted', 'rb') as file:
        file_contents = file.read()
    data_key_encrypted_len = int.from_bytes(file_contents[:NUM_BYTES_FOR_LEN],
                                            byteorder='big') + NUM_BYTES_FOR_LEN
    data_key_encrypted = file_contents[NUM_BYTES_FOR_LEN:data_key_encrypted_len]
    # Decrypt the data key before using it
    data_key_plaintext = decrypt_data_key(data_key_encrypted)
    # Decrypt the rest of the file
    f = Fernet(data_key_plaintext)
    file_contents_decrypted = f.decrypt(file_contents[data_key_encrypted_len:])
    # Write the decrypted file contents
    with open(FILENAME + '.decrypted', 'wb') as file_decrypted:
        file_decrypted.write(file_contents_decrypted)
        
encrypt_file()
decrypt_file()