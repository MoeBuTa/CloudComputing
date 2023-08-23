IAM user: use access key ID and secret access key as credentials

IAM role: align with permission policies that determine allow and deny rules. - assigned to anyone who needs it.

IAM user group: specify permission policies to a group of users.

IAM policy: policies attach to IAM identities (user, group, role)



CAF: 
 - Business
 - People
 - Grovernance
 - Platform
 - Security
 - Operations


Service Catalog: create and manage catalogs of IT services ( virtual machine images, servers, software, databases).

APN: AWS Partner Network. technology and consulting businesses to build **solutions** and services for customers.

AWS Organisations: centrally management. (manage billing, control access, compliance, security, share resource across AWS accounts).

CloudWatch: resource performance monitoring, events, and alerts.

CloudTrail: account-specific activity and audit.

encryption:
 - automatically enabled: 
   - storage gateway, 
   - S3
   - cloudtrail logs stored in s3
 - optional: 
   - EBS, 
   - Redshift, 
   - EFS


Virtual MFA device: A software app that emulates a physical device.

U2F security key: A device that you plug into a USB port on your computer.


Amazon CloudWatch Logs enables you to centralize the logs from all of your systems, applications, and AWS services that you use, in a single, highly scalable service.

AWS CloudTrail cannot be used to centralize the server logs for Amazon Elastic Compute Cloud (Amazon EC2) instances or on-premises servers.

Shield standard:  enabled for all AWS customers at no additional cost.

WAF: HTTP/HTTPS requests forwarding to API gateway, cloudfront, ALB. (no route 53)

Credential report: list all users in the account and the status of their credentials.

Artifact: download security and compliance related information
 - reports: Service Organization Control (SOC) reports, Payment Card Industry (PCI) reports, and certifications from accreditation bodies


VPC interface endpoint: 
 - VPC -> services
 - powered by **PrivateLink** - no public internet, support S3

VPC gateway endpoint: 
 - VPC -> services
 - only support **S3**, **dynamoDB**.


Trusted Advisor alerts when:
 -  leaving certain ports open that make you vulnerable
 -  neglecting to create IAM accounts for your internal users
 -  allowing public access to Amazon S3 buckets
 -  not turning on user activity logging (AWS CloudTrail)
 -  not using MFA on your root AWS Account.

IAM user access keys: 
 - long-term credentials
 - global service
 - not suitable for accessing dynamoDB - temporary credentials are better (IAM role)

Cognito: 
 - add user credential to web apps.
 - cannot be used to access dynamoDB.

CloudHSM: 
 - generate, store, manage credentials

Secret manager: 
 - protect credentials for applications and services
 - manage credentials (rotate, retrieve, manage)
 - integrate with CloudHSM

Macie: 
 - data discovery and protection in Amazon S3 (Simple Storage Service) buckets
 - automatically discover, classify, and protect sensitive data in S3.

Detective: 
 - analyse events 
 - identify potential security issues.
 - cloudtrail logs, VPC flow logs, guardduty findings


