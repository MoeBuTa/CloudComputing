import boto3

client = boto3.client('kms')

# create kms key
keyInfo = client.create_key(
    Description='22792191-kms-key', 
    Tags=[{
        'TagKey':'Name',
        'TagValue':'22792191-kms-key'
}])
key_id = keyInfo['KeyMetadata']['KeyId']
key_region =  keyInfo['KeyMetadata']['Arn']

# create alias
client.create_alias(AliasName='alias/22792191', TargetKeyId=key_id)

print('key_id is:' + key_id)
print('key_region is: '+ key_region)
