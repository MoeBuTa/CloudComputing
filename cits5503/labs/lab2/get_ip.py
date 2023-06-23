import boto3

AWS_REGION = "ap-southeast-2"
AMI_ID ="ami-d38a4ab1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
KEY_PAIR_NAME = "Z22792191"
SECURITY_GROUP_ID = 'sg-02e03d15c337cfec2'
INSTANCE_ID = 'i-02aff76e37b24898c'

EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)

response = EC2_CLIENT.describe_instances(
    InstanceIds=[
        INSTANCE_ID
    ],
)
print(response['Reservations'][0]['Instances'][0]['PublicIpAddress'])
