import boto3

AWS_REGION = "ap-southeast-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
SECURITY_GROUP_ID = 'sg-02e03d15c337cfec2'

key_pair = EC2_RESOURCE.create_key_pair(
    KeyName='Z22792191',
    TagSpecifications=[
        {
            'ResourceType': 'key-pair',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Z22792191'
                },
            ]
        },
    ]
)
print( key_pair.key_fingerprint)
print(key_pair.key_material)