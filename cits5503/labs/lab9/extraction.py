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


def text_extraction(img):
    response = client.detect_text(Image=img)
    print('text extraction for %s:' % img['S3Object']['Name'])
    print(response['TextDetections'])
    print()
    
text_extraction(imgs[0])
text_extraction(imgs[1])
text_extraction(imgs[2])
text_extraction(imgs[3])
