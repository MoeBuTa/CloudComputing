# CITS5503 Lab2 
## Wenxiao Zhang 22792191

<br>

## Create an EC2 instance using awscli

### [1] Create a security group
![image](1.1.png)
### [2] Authorise inbound traffic for ssh
![image](1.2.png)
### [3] Create a key pair that will allow you to ssh to the EC2 instance
we make a directory named `.ssh`, then copy the key pair to the directory.
![image](1.3.png)
### [4] Create the instance and note the instance id
![image](1.4.png)
add a tag to the instance:
![image](1.4.1.png)
### [5] Get the public IP address
![image](1.5.png)
### [6] Connect to the instance
![image](1.6.png)
### [7] Look at the instance using the AWS console
![image](1.7.png)
![image](1.7.1.png)
### [8] Terminate the instance
![image](1.8.png)

## Create an EC2 instance with Python Boto script

### Repeat the steps above using the equivalent Boto commands in a python script. The script should output the IP address to connect to.
### Step 1 – Create a security group
python code:
![image](3.1.1.png)
output:
![image](3.1.png)

### Step 2 - Authorise inbound traffic for ssh, from port/to port 22 indicates ssh, and CidrIp 0.0.0.0/0 indicates directions
python code:
![image](3.2.1.png)
output:
![image](3.2.png)
### Step 3 – Create the key pair via create_key_pair function to allow ssh into EC2 instance
python code:
![image](3.3.1.png)
output:
![image](3.3.png)
<div style="page-break-after: always;"></div>

### Step 4 – Create the instance via run_instance function and return the instance id
python code:
![image](3.4.1.png)
output:
![image](3.4.png)

AWS console:
![image](3.5.png)

![image](3.5.1.png)
Step 5 – Return the public IP of the instance created from previous steps via describe_instance function
python code:
![image](3.6.1.png)
output:
![image](3.6.png)

## Using Docker

### [1] Install Docker
![image](2.1.png)
### [2] Check the version
![image](2.2.png)
### [3] Build and run an httpd container
we make a directory named `html`, then create `index.html` using `touch` command, then edit `index.html` using `nano` command, then we print the content of `index.html` using `cat` command.
![image](2.3.png)
### [4] Create a file called “Dockerfile” outside the html directory with the following content:
We use `touch` command to create `Dockerfile`, then use `nano` to edit it, then we print the content of `Dockerfile` using `cat` command.
![image](2.4.png)
### [5] Build the docker image
![image](2.5.png)
### [6] Run the image
![image](2.6.png)
### [7] Open a browser and access address http://localhost Confirm you get Hello World!
![image](2.7.png)
### [8] Other commands
![image](2.8.png)

