# CITS5503 Lab5
## Wenxiao Zhang 22792191



## Step 1: Configure a target group

For Choose a target type, select Instance to specify targets by instance ID
![image](1.1.png)

For Target group name, enter a name for the target group.

![image](1.2.png)

the rest settings are set as default.

![image](1.3.png)

## Step 2: Register targets

Create 2 ec2 instances using aws console:

The first one named `22792191 - a`, availability zone is `ap-southest-2a`
key pair `22792191-key`, port 80, security group `22792191-sg`
![image](2.1.1.png)

![image](2.1.2.png)

The second one named `22792191 - b`, availability zone is `ap-southest-2b`
key pair `22792191-key`, port 80, security group `22792191-sg`
![image](2.1.3.png)

![image](2.1.4.png)

Register targets using the created 2 instances

![image](2.1.png)


![image](2.2.png)


## Step 3: Configure a load balancer and a listener

Under Application Load Balancer, choose Create

![image](3.1.png)

**Basic configuration**

Naming the load balancer: 22792191-lb

scheme: internet-facing

IP address type: IPv4
![image](3.2.png)

**Network mapping**

select 2 Availability Zones and corresponding subnets: 'ap-southeast-2a' and 'ap-southeast-2b'

![image](3.3.png)


**Security Group**

select an existing security group '22792191-sg'
![image](3.4.png)

**Listeners and routing**

use default settings
![image](3.5.png)


**Summary and Create**

![image](3.6.png)

successful page:

![image](3.7.png)


Install `apache2` to instance `22792191 - a`:

![image](3.8.1.png)
![image](3.8.2.png)
![image](3.8.3.png)

Install `apache2` to instance `22792191 - b`:

![image](3.8.4.png)
![image](3.8.5.png)
![image](3.8.6.png)

Check registered targets

![image](3.9.png)
## Step 4: Test the load balancer

Choose Targets and verify that the instances are ready.


![image](4.1.png)

Select the new created load balancer
![image](4.2.png)

Choose Description and copy the DNS name of the load balancer

http://22792191-lb-707575599.ap-southeast-2.elb.amazonaws.com/

![image](4.3.png)

Delete load balancer and terminate ec2 instances

![image](4.4.png)

![image](4.5.1.png)

terminate `22792191 - a`
![image](4.5.2.png)

![image](4.5.3.png)

terminate `22792191 - b`
![image](4.5.4.png)
![image](4.5.5.png)