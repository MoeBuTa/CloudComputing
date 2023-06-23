import boto3
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


def label_detection(img):
    response = client.detect_labels(Image=img, MaxLabels=3, MinConfidence=0.95)
    print('label detection for %s:' % img['S3Object']['Name'])
    print(response['Labels'])
    print()
    
label_detection(imgs[0])
label_detection(imgs[1])
label_detection(imgs[2])
label_detection(imgs[3])
