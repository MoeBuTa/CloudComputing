cloud foundations: 
 - guide deploy, configure, secure workloads while **ensuring operations in the cloud**
 - navigate decisions (AWS Solutions, Partner Solutions, Guidance)

Trusted Advisor: 
 - guide provision resources **following best practices**
 - five categories:
   - cost optimisation
   - performance
   - security
   - fault tolerance
   - service limits

Transit gateway:
 - VPC -> on-premise 
 - through a central hub
 - can interconnect VPCs

Direct Connect:
 - VPC -> on-premise
 - private connection - not use public internet 
 - cannot interconnect VPCs

VPC peering connection:
 - VPC -> VPC
 - not transitive - difficult to manage

VPC interface endpoint: 
 - VPC -> AWS Services
 - powered by **PrivateLink** - no public internet, support S3

VPC gateway endpoint: 
 - VPC -> AWS Services
 - only support **S3**, **dynamoDB**.

Internet gateway:
 - VPC -> public internet

API gateway:
 - VPC internal service -> clients





Site-to-Site VPN:
 - AWS Services -> on-premise
 - cannot interconnect VPCs
 - components: 
   - virtual private gateway, 
   - transit gateway, 
   - customer gateway, 
   - customer gateway device




AWS cost and usage report:
 - generate billing reports that break down 
   - by hour or month, 
   - by product or product resource, 
   - by tags
 - cannot be used to identify under-utilized Amazon EC2 instances.

AWS Knowledge Center contains the most frequent & common questions and requests and AWS provided solutions for the same.

AWS Support Center is the hub for managing your Support cases. 

Global Accelerator:
 - low latency - high performance
 - high availability
 - static IP address
 - non-HTTP use cases (UDP, MQTT)

S3 transfer Acceleration (S3TA):
 - powered by cloudfront
 - client - S3 bucket
 - not for replicating data

LB: distribute traffic, not scale resources

Warm standby: 
 - can handle traffic at reduced levels immediately. 

Pilot light: 
 - cannot serve requests until additional steps are taken
   - deploy infrastructure and 
   - scale out resources 
   - then workload can handle requests.


Cloud Adoption Framework (CAF):
- Business, 
- People,  
- Governance
- Platform, 
- Security, 
- Operations

CAF stakeholders: CTO, technology leaders, architects, engineers.

6 Pillars:
1.Operational excellence (Cloudformation): **run** systems to deliver business value.
2.Security (IAM, WAF, KMS): **protect** system while deliver business value
3.Relibility (IAM, Cloudformation, S3): the ability of a system to **recover**
4.Performance efficiency(auto scaling, lambda, elasticache): **use computing resources** efficiently
5.Cost optimisation (budget, cost explorer): run systems at the lowest **price** point
6.Sustainability (auto scaling, fargate, s3, ec2): minimise the **environmental** impacts

recovery time objective: 
 - real-time: Multi-site active/active (run simultaneously)
 - minutes: warm standby (scaled-down but full functional copy)
 - 10s of minutes: pilot light (core component)
 - hours: backup & restore (data only, need redeploy infrastructure)

local zone: 
 - low latency to specific geographic areas
 - optimise latency
 - gaming

outpost:
 - low latency to on-premises location
 - run service locally

well-architected tool:
 - review the state of your workloads
 - compare with best practices

WorkSpaces:
 - global services
 - provision Windows or Linux desktops

Athena:
 - query service
 - serverless
 - facilitate analyse data in S3