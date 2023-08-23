# CITS5503 Lab9
## Wenxiao Zhang 22792191


## **[Step 1] Detecting Languages from text**


### **[Step 1.1] Modify code**

install `iso-639`

![image](1.1.png)

Write a script to recognize different languages and return the message in designated format.

![image](1.2.png)

## **[Step 1.2] Test code with other languages**


Spanish:

![image](1.3.png)

French:

![image](1.4.png)

Italian:

![image](1.5.png)

## **[Step 2] Sentiment Analysis**

Use boto3 and AWS comprehend to create a python script for sentiment analysis.

![image](2.1.png)

## **[Step 3] Repeat steps from [Step 2] for detecting entities.**

python script:

![image](3.1.png)


output:

![image](3.2.png)

## **[Step 4] Repeat steps from [Step 2] for detecting keyphrases.**

python script:

![image](4.1.png)

output:

![image](4.2.png)


## **[Step 5] Repeat steps from [Step 2] for detecting syntax.**


python script:

![image](5.1.png)

output:

![image](5.2.png)


## **[Step 6] In an S3 bucket add some images to test algorithms.**

Upload images to the bucket via AWS console

![image](6.1.png)

![image](6.2.png)




## **[Step 7] Create scripts using boto3 and rekognition to test label recognition, image moderation, facial analysis and extracting text from images.**

<div style="page-break-after: always;"></div>

Label recongnition:

![image](7.1.png)

output:
![image](7.2.png)

<div style="page-break-after: always;"></div>

Image moderation:

![image](7.3.png)

output:
![image](7.4.png)

<div style="page-break-after: always;"></div>

Facial analysis:

![image](7.5.png)

output:
![image](7.6.png)

<div style="page-break-after: always;"></div>

Extracting text from images:

![image](7.7.png)

output:
![image](7.8.png)

![image](7.9.png)
