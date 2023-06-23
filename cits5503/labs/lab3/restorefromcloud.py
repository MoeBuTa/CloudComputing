import os
import boto3
ROOT_DIR = '.'
ROOT_S3_DIR = '22792191-cloudstorage'

s3 = boto3.client("s3")
bucket_config = {'LocationConstraint': 'ap-southeast-2'}

for key in s3.list_objects(Bucket = ROOT_S3_DIR)['Contents']:
    print("Downloading %s" % key['Key'])
    if not os.path.exists(os.path.dirname(key['Key'])):
        os.makedirs(os.path.dirname(key['Key']))
    s3.download_file(ROOT_S3_DIR, key['Key'],  key['Key'])

    