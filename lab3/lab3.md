# CITS5503 Lab3 
## Wenxiao Zhang 22792191

<br>

### [Step 1] Preparation

Download the python code cloudstorage.py from https://github.com/dglance/cits5503/blob/master/Labs/src/cloudstorage.py



Create a directory rootdir

![image](1.1.png)

Create a file in rootdir called rootfile.txt and put some content in it “1\n2\n3\n4\n5\n”

Create a second directory in rootdir called subdir and create another file subfile.txt with the same content as rootfile.txt

![image](1.2.png)

<div style="page-break-after: always;"></div>

### [Step 2] Save to S3

Edit cloudstorage.py to take one argument: -i, --initialise=True – this will use boto to create a bucket on S3 that is identified by 22792191-cloudstorage

Insert boto commands to save each file that is found as the program traverses the directory starting at the root directory rootdir.


python code:
![image](2.0.png)

output for creating a bucket with student number:
![image](2.1.1.png)

output for save each file:
![image](2.2.1.png)

Open AWS console to confirm:
![image](2.3.png)
![image](2.3.1.png)
![image](2.3.2.png)



### [Step 3] Restore from S3

Create a new program called restorefromcloud.py that reads the S3 bucket and writes the contents of the bucket within the appropriate directories. You should have a copy of the files and the directories you started with.

python code:
![image](3.1.png)

output:
![image](3.2.png)
### [Step 4] Write information about files to DynamoDB

Install DynamoDB on your VM.

mkdir dynamodb;

cd dynamodb

Install jre if not done

sudo apt-get install default-jre

wget https://s3-ap-northeast-1.amazonaws.com/dynamodb-local-tokyo/dynamodb_local_latest.tar.gz

![image](4.1.png)

java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar –sharedDb

![image](4.2.png)

Create a table on your local DynamoDB with the key userId The attributes for the table will be:

        CloudFiles = {
            'userId',
            'fileName',
            'path',
            'lastUpdated',
	    'owner',
            'permissions'
            }
        )

For every file that is stored in S3, get the information to put in the DynamoDB item and write it to the table. You will have to find functions in Python to get details like time lastUpdated, owner and permissions. All of this information can be stored as strings.

<div style="page-break-after: always;"></div>

Creating table:
We set `CloudFiles` to be the table name, `userId` to be the partition key, and `fileName` to be the sort key. 
![image](4.3.png)

Python code to extract user information from bucket and put them into the local dynamoDB:
![image](4.4.png)


<div style="page-break-after: always;"></div>


Output:
![image](4.5.png)

Scan the content of the local table:
![image](4.6.png)