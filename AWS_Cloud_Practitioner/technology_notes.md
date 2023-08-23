Root user cannot be restricted

Elastic Beanstalk: PaaS. an engine to deploy and scale services.

CloudFormation: 
 - infrastructure as code. (a broader concept, can include IaaS)
 - automate the provisioning and management of resources across various AWS services
 - can estimate costs using templates

ECS: 
 - a container management service.  
 - a platform for deploying and managing containerized applications, 
 - leveraging Docker containers, and orchestrating their deployment and scaling.

Amazon MQ: message broker for moving messaging functionality from on-premise application to cloud.

SQS: 
 - move data between components. 
 - help build applications with independent message processing.

SNS:
 - messaging service for application-application and application-person communication

Compute optimizer: 
 - EC2, 
 - Auto Scaling group, 
 - EBS, 
 - Lambda

Storage gateway: 
 - bridge on-premise data and cloud data in S3
 - File, Volume, Tape

Step function: 
 - coordinate multiple AWS services (sagemaker, glue, lambda) into serverless workflows. 
 - Cannot be used to run a process on a schedule.

Database:
 - Glue: prepare and transform data for analytics, serverless
 - Neptune: **graph** database
 - Quantum Ledger Database (QLDB): review history of all changes made to application data
 - Database Migration Service (DMS)
 - Athena: serverless query service to perform analytics against **S3 objects**
 - EMR: Elastic MapReduce - analyse and process big data, **hadoop cluster**
 - Redshift: SQL analytics and cloud data **warehousing**
 - Aurora: MySQL and PostgreSQL
 - DocumentDB: Aurora version for **MongoDB**
 - QuickSight: create interactive **dashboards** on database
 - ElastiCache: **in-memory** database

Security group: 
 - stateful
 - instance level
 - allow rule only

NACL:
 - stateless
 - subnet level
 - allow and deny rules



Read Replicas:
 - used for improved read performance. - scalability
 - horizontal scaling

Amazon EFS 
 - keeping files accessible to satisfy audit requirements, 
 - performing historical analysis, 
 - or performing backup and recovery. 
 - EC2 instances can access EFS across AZs, regions, and VPCs, 
 - while on-premises servers can access using AWS Direct Connect or AWS VPN. 
 - cannot be used as a boot volume for Amazon Elastic Compute Cloud (Amazon EC2) instances. 
 - For boot volumes, Amazon Elastic Block Storage (Amazon EBS) volumes are used.


Amazon Kendra: 
 - **search service** in unstructured data - accurate search results.

Amazon Personalize 
 - **building applications** with personalized recommendations capability.

Amazon Comprehend 
 - **extracting insights** in unstructured data - help understanding. 
 - NLP
 - text analysis, topic modelling, keyphrase extraction, syntax analysis...

Amazon Lex
 - **building conversational interfaces** into any application using voice and text. 
 - NLU
 - chatbot

A customer gateway is **a resource in AWS** that provides information to AWS about your Customer gateway device.

Site-to-Side VPN components:
 - virtual private gateway
 - transit gateway
 - customer gateway
 - customer gateway device

Global scope services:
 - EC2, S3, DynamoDB, SNS, IAM, CloudFront, Route 53, WAF...

Regional scope services:
 - lambda, redshift, read replicas, rekognition


 The pricing for an AWS Lambda function is not dependent on the language runtime of the function.

 AWS CodeDeploy is a service that automates code deployments to any instance,

 CloudFormation cannot be used to automate code deployment.

 EBS: 
  - A broad range of workloads, such as relational and non-relational databases, enterprise applications, containerized applications, big data analytics engines, file systems, and media workflows are widely deployed on Amazon EBS.
  - not a good fit for caching information on Amazon EC2 instances

S3 actions:
 - transition actions:  

partner solutions: 
 - automated technology deployments

whitepapers: 
 - technical content (technical guides, reference materials, architecture diagrams)

route 53:
 - domain registration
 - health check and monitoring

AWS Health:
 - Performance and availability of AWS services 

IAM Identity Center:
 - successor to sso

DataSync:
 - simplifies and accelerates moving data between on-premises storage systems and AWS services

EC2 instance user data:
 - data specified in the form of a **bootstrap script** configuration parameters while launching your instance

EC2 instance metadata:
 - data about your instance you can use to **manage the instance** (ami-id, public-hostname)


S3 no retrieval fee:
 -  intelligent-tiering
 -  standard

read-replicas:
 - create read-only copies with master database
 - place in different AWS region
 - improve performance
 - data recovery

