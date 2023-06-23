import boto3

ROOT_S3_DIR = '22792191-cloudstorage'
TABLE = 'CloudFiles'

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2', endpoint_url='http://localhost:8000')
table = dynamodb.Table(TABLE)
s3 = boto3.client('s3')
response = s3.list_objects(Bucket=ROOT_S3_DIR)

userId = str(response['Contents'][0]['Owner']['ID'])
owner = response['Contents'][0]['Owner']['DisplayName']
permission = s3.get_bucket_acl(Bucket=ROOT_S3_DIR)['Grants'][0]['Permission']

i = 1
for content in response['Contents']:
    item = {
        'id': i,
        'userId':userId,
        'fileName': content['Key'].split('/')[-1],
        'path': content['Key'],
        'lastUpdated': str(content['LastModified']),
        'owner': owner,
        'permissions': permission
    }
    print('puting the following item into CloudFiles table:\n', item, '\n')
    i+=1
    table.put_item(Item = item)
print('done!')



