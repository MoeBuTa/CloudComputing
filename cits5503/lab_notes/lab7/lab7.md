# CITS5503 Lab7
## Wenxiao Zhang 22792191

## **[Step 1] Create an EC2 instance**

we use AWS console to create an EC2 instance:

![image](1.0.1.png)

![image](1.0.2.png)

![image](1.0.3.png)

## **[Step 2] Install and configure Fabric on your VM**


![image](2.1.png)

Create a file named `config` in ~/.ssh and add the following contents to it:

![image](2.2.png)

Test fabric from the command line:

![image](2.3.png)

## **[Step 3] Write a python script to automate the installation of nginx**

Write a script `config_nginx.py` for automate installation of nginx.

![image](3.1.png)


## **[Step 4] Update the python script to install your Django app**

Create a file named `default` and edit the content to prepare for uploading to the ec2 instance.

![image](3.2.png)

Extend `config_nginx.py` script for replace the default file with local file.

![image](3.3.png)

Write another script to config and run Django.

![image](3.4.png)

We can see the django server is deployed successfully by accessing the ip address of the instance.


![image](3.5.png)

Now we need to write code to update the code in the django. We will edit `polls/views.py`, `polls/urls.py`, and `lab/urls.py`

![image](3.6.png)

![image](3.7.png)

![image](3.8.png)

Then we write a script to update the code to the instance:

![image](3.9.png)

We can see the 'Hello world!!' is displayed in the webpage by accessing the ip address of the instance.

![image](3.10.png)

## **[Step 5] Terminate the instance**

![image](3.11.png)

![image](3.12.png)