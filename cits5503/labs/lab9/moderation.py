import boto3
from chardet import detect
client = boto3.client('rekognition')

imgs=[
    {
        'S3Object': {
            'Bucket': '22792191-cloudstorage',
            'Name': 'Urban setting.jpg'
        },
    },
    {
        'S3Object': {
            'Bucket': '22792191-cloudstorage',
            'Name': 'a person on the beach.jpg'
        },
    },    
    {
        'S3Object': {
            'Bucket': '22792191-cloudstorage',
            'Name': 'image with text.jpg'
        },
    },
    {
        'S3Object': {
            'Bucket': '22792191-cloudstorage',
            'Name': 'people showing their faces.jpg'
        },
    },        
    ]


def img_moderation(img):
    response = client.detect_moderation_labels(Image=img)
    print('image moderation for %s:' % img['S3Object']['Name'])
    print(response['ModerationLabels'])
    print()
    
img_moderation(imgs[0])
img_moderation(imgs[1])
img_moderation(imgs[2])
img_moderation(imgs[3])
