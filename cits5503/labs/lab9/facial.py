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


def facial_analysis(img):
    response = client.detect_faces(Image=img)
    print('facial analysis for %s:' % img['S3Object']['Name'])
    print(response['FaceDetails'])
    print()
    
facial_analysis(imgs[0])
facial_analysis(imgs[1])
facial_analysis(imgs[2])
facial_analysis(imgs[3])
