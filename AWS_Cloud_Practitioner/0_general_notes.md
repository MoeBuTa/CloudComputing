EC2 instance: 
 - m5.2xlarge: m: instance class, 5: generation, 2xlarge: size within the instance class (cpu, ram..)
 - compute optimised: c name
 - memory optimised: 
 	- database
- cache stores
 - storage optimised:
 - online transaction processing system
 - database
 - data warehousing
- instance connect: SSH based browser session connection
- purchasing options:
 - on-demand: short workload, predictable pricing
 - reserved (1 & 3 years): long workload
 - savings plans (1 & 3 years): commitment to an amount of usage
 - spot instances: cheap, less reliable, bid
 - dedicated hosts: physical server
 - dedicated instances: no others share hardware
 - capacity reservations: reserve capacity in a specific AZ for any duration

EC2 Instance Storage
 - EBS volumes: attach to one EC2, one AZ
 - AMI ( amazon machine image): EC2 instances image, a customisation of EC2
 - EC2 Image Builder: build, test, distribute AMIs
 - EC2 Instance Store: hardware disk
 - EFS: managed network file system, mounted on 100 EC2 in multi-AZ

Permissions:

IAM:
Security group: instance level, only allow rules, stateful (specify inbound is enough)
NACL: subnet level, allow and deny rules, stateless (both inbound and outbound need to specify)

Machine learning:
 - Polly: converts text into speech
 - Transcribe: convert speech into text


Responsibility Model:

AWS: 
- security of the cloud: physical infrastructure, network, foundational components (host os)
Customer: 
- security in the cloud: application, data encryption, access control, service/network configurations. 


S3:
- Security:
 - user-based: IAM
 - resource-based: Bucket policies (JSON allow/deny), object ACL, bucket ACL

- Replication: Cross-region R, Same-region R

- Solutions:
- Standard: high availability, frequent access
- IA: less frequent but rapid access, low cost for recovery/backup
- Standard: high availability
- One Zone: lower cost
- Glacier: low cost for archiving/backup
- Intelligent-Tiering: move objects automatically between tiers based on usage
- frequent access tier, infrequent access tier, archive instant access tier, archive access tier

- Snow family: offline devices for data migrations
 - snowcone: 8TB
 - snowball edge: 80TB
 - snowmobile: 100PB

- Storage gateway: bridge on-premise data and cloud data in S3
 - File, Volume, Tape


6 Pillars:
1.Operational excellence (Cloudformation): run systems to deliver business value.
2.Security (IAM, WAF, KMS): protect system while deliver business value
3.Relibility (IAM, Cloudformation, S3): the ability of a system to recover
4.Performance efficiency(auto scaling, lambda, elasticache): use computing resources efficiently
5.Cost optimisation (budget, cost explorer): run systems at the lowest price point
6.Sustainability (auto scaling, fargate, s3, ec2): minimise the environmental impacts

Cloud Adoption Framework (CAF):
- Business, 
- People,  
- Governance
- Platform, 
- Security, 
- Operations


Database:
- Glue: prepare and transform data for analytics, serverless
- Neptune: graph database
- Quantum Ledger Database (QLDB): review history of all changes made to application data
- Database Migration Service (DMS)
- Athena: serverless query service to perform analytics against S3 objects
- EMR: Elastic MapReduce - analyse and process big data, hadoop cluster
- Redshift: SQL analytics and cloud data warehousing
- Aurora: MySQL and PostgreSQL
- DocumentDB: Aurora version for MongoDB
- QuickSight: create interactive dashboards on database
- ElastiCache: in-memory database


AWS Shield Advanced: network layer, transport layer, application layer.
 - EC2, ELB, CloudFront, route 53, global accelerator

API Gateway: front door. WAF monitor requests forwarded to API gateway. Not covered under AWS shield.

APN: global partner program for technology and consulting to build solutions
 - e.g. move infrastructure from on-premises data center to AWS cloud.


AWS Support Plan:

Developer: testing or doing early development, email-based support during business hours

Business: production workload on AWS, 24x7 phone, email and chat support, Trusted Advisor

Enterprise On-Ramp: application service, production/business critical workloads in AWS, 24x7 support

Enterprise: application service, 24x7 support from engineers to automatically manage

CAF stakeholders: CTO, technology leaders, architects, engineers.

Customer Managed Key (CMK): create, own, managing key policies, IAM
Secret manager
Managed key
Owned key


CloudFormation: need to specify the resource you want to provision

Amazon MQ: message broker service that makes it easy to set up and operate message brokers.

Developer: one contact + unlimited cases
Business, On-Ramp, Enterprise: unlimited contacts + unlimited cases

Compute optimizer: EC2, Auto Scaling group, EBS, Lambda

AWS step function: coordinate multiple AWS services into serverless workflows. Cannot be used to run a process on a schedule. Cannot decouple components

System Manager Session Manager: interactive browser-based shell and cli.
Instance connect: connect instance using SSH. Need port 22



