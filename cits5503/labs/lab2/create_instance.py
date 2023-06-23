import boto3

AWS_REGION = "ap-southeast-2"
AMI_ID ="ami-d38a4ab1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
KEY_PAIR_NAME = "Z22792191"
SECURITY_GROUP_ID = 'sg-02e03d15c337cfec2'

EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)

instances = EC2_RESOURCE.create_instances(
    MinCount = 1,
    MaxCount = 1,
    ImageId=AMI_ID,
    InstanceType='t2.micro',
    KeyName=KEY_PAIR_NAME,
    SecurityGroupIds=[
        SECURITY_GROUP_ID,
    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': '22792191'
                },
            ]
        },
    ]
)
for instance in instances:
    print(instance.id)