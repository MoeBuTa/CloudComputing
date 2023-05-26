# CITS5503 Lab6
## Wenxiao Zhang 22792191



## **Step 1: Create an EC2 instance**


**1.1 Create an EC2 micro instance using Ubuntu and SSH into it.**

using AWS console to launch an instance

![image](1.1.png)

![image](1.1.1.png)

![image](1.1.2.png)

![image](1.1.3.png)

using Ubuntu and SSH into it

![image](1.1.4.png)

**1.2 update package and install python venv**
   
![image](1.2.png)

![image](1.3.png)

![image](1.4.png)

**1.3 install python pip**

![image](1.5.png)

**1.4 Create a directory with a path /opt/wwc/mysites and cd into that. Set up a virtual environment.**

we can see that the directories are all listed properly:

![image](1.6.png)

Activate the virtual environment and install django:

![image](1.7.png)

we can see 3 items: lab, manage.py and polls under the lab project,
and items: __init__.py, admin.py, apps.py, migrations, models.py, tests.py and views.py under `polls` directory.
![image](1.8.png)

<div style="page-break-after: always;"></div>

## **Step 2: Install and configure nginx (under polls)**

![image](2.1.png)

![image](2.1.1.png)

![image](2.2.png)

![image](2.3.png)

![image](2.4.png)

<div style="page-break-after: always;"></div>


## **Step 3:  Changing the code**

Edit polls/views.py (just an example)
Under lab type vim polls/views.py

![image](2.5.png)

![image](2.6.png)

Edit polls/urls.py
Under lab, type vim polls/urls.py

![image](2.7.png)

![image](2.8.png)

Edit lab/urls.py
Under lab, type vim lab/urls.py

![image](2.9.png)

![image](2.10.png)

Now run `python3 manage.py runserver 8000`

![image](2.11.png)

![image](2.12.png)

<div style="page-break-after: always;"></div>


## **Step 4: Create a load balancer**

use AWS console to create a load balancer named `22792191-lb`


![image](4.2.png)

![image](4.3.png)

![image](4.4.png)

![image](4.5.png)

Change the path of the health check of the target group

![image](4.6.png)


Register the instance into the target group `22792191-tg`

![image](4.1.png)

We can see that the instance is healthy now
![image](4.7.png)

Delete load balancer

![image](4.8.png)

![image](4.9.png)


<div style="page-break-after: always;"></div>

## **Extension step**


configure aws in the instance

![image](5.5.png)

![image](5.6.png)


Install DynamoDB and JRE in the instance

![image](5.1.png)

![image](5.2.png)

![image](5.3.png)

![image](5.4.png)

Create a table in DynamoDB

![image](5.7.png)

Insert an element into the DynamoDB

![image](5.8.png)

scan the table to see the element

![image](5.9.png)

install boto3

![image](5.10.png)


Modify code in `polls/views.py`

![image](5.11.png)

Modify nginx proxy port number into 8001 and restart service

![image](5.12.png)

![image](5.13.png)

Deploy Django in 8001 port

![image](5.14.png)

Open the browser and we can see the `elementName` value: "test" is displayed in the browser.

![image](5.15.png)






