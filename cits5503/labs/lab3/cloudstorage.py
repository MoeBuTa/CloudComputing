from ast import parse
import os
from py_compile import main
import boto3
import base64
import argparse
import logging
from botocore.exceptions import ClientError

ROOT_DIR = '.'
ROOT_S3_DIR = '22792191-cloudstorage'

s3 = boto3.client("s3")
bucket_config = {'LocationConstraint': 'ap-southeast-2'}

def upload_file(folder_name, file, file_name):
    print("Uploading %s" % file)
    try:
        s3.upload_file(file,ROOT_S3_DIR, folder_name+file_name)
    except ClientError as e:
        logging.error(e)

def parse_args():
    parser = argparse.ArgumentParser(description="arg parser")
    parser.add_argument("-i", "--initialise", default=True, type=bool)
    return parser.parse_args()

# Main program
# Insert code to create bucket if not there
def main():
    args = parse_args()
    if args.initialise:
        try:
            response = s3.create_bucket(Bucket=ROOT_S3_DIR, CreateBucketConfiguration=bucket_config)
            print(response)
        except Exception as error:
            pass

    # parse directory and upload files
    for dir_name, subdir_list, file_list in os.walk(ROOT_DIR, topdown=True):
        if dir_name != ROOT_DIR:
            for fname in file_list:             
                upload_file("%s/" % dir_name[2:], "%s/%s" % (dir_name, fname), fname)
    print("done")

if __name__ == "__main__":
    main()