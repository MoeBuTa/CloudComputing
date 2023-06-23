import boto3

AWS_REGION = "ap-southeast-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)

security_group = EC2_RESOURCE.create_security_group(
    Description='Allow inbound SSH traffic',
    GroupName='22792191',
    TagSpecifications=[
        {
            'ResourceType': 'security-group',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': '22792191'
                },
            ]
        },
    ],
)

print(f'Security Group Created {security_group.id} has been created in vpc {security_group.vpc_id}')