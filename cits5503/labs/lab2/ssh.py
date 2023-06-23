import boto3

AWS_REGION = "ap-southeast-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
SECURITY_GROUP_ID = 'sg-02e03d15c337cfec2'

security_group = EC2_RESOURCE.SecurityGroup(SECURITY_GROUP_ID)


response = security_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=22,
    ToPort=22,
    IpProtocol='tcp',
)
print(f'Ingress successfully set {response}')