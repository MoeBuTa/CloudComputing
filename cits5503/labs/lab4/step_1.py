import boto3
import json

BUCKET = '22792191-cloudstorage'
s3 = boto3.client("s3")

bucket_policy = {
    "Version": "2012-10-17",
    "Statement": {
    "Sid": "AllowAllS3ActionsInUserFolderForUserOnly",
    "Effect": "DENY",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": "arn:aws:s3:::22792191-cloudstorage/*",
    "Condition": {
      "StringNotLike": {
          "aws:username":"22792191@student.uwa.edu.au"
       }
    }
  }
}

bucket_policy = json.dumps(bucket_policy)

s3.put_bucket_policy(Bucket=BUCKET, Policy=bucket_policy)
result = s3.get_bucket_policy(Bucket=BUCKET)
print(result['Policy'])
