## 1. (20 points)
The creative designers of a marketing and video editing company in Melbourne use a commercial web-based application for converting videos to different formats.  In addition, one of the  main advantages of this software is the ability to publish those videos in popular social media networks such as YouTube, Instagram, Twitter, etc. This allows the user to convert and edit a video and then publish the same video at the same time to all different social media that the user selects in the software. This is particularly useful for marketing campaigns were usually a video is published in different social media networks. In the past, before using that software they used to spend around 5-10 hours  to convert a single video to different formats, resolutions, etc. and upload them to all different social media. Now using this software this process is reduced to only 45mins to  1 hour. Since they started using this software, they have to pay a monthly subscription fee of 25.000 AUD per month or around 300.000 AUD per year regardless of the number of videos they process per year. Despite all the benefits from this software, the CTO of the company believes they should pay a software developer to replicate this web-based software instead of keep paying those high fees. While he knows building software is expensive, he also believes there must be a way of designing this new software to reduce the cost and make it profitable in the long term. You as a Software Developer and Cloud Computing expert are hired for this task.
#### **1.1  (10 points) You initially think on using EC2 instances for processing. Briefly explain what other AWS technologies you would use to replicate the web-based software functionalities and what architecture you would use to satisfy the needs of the client using such technologies.**
 
1. Using ec2 instances to host the web server. the process of publish videos into different social media platforms can be automated via ec2 instances.
2. S3 bucket will be implemented to store the videos.
3. Elastic transcoder will be used to transform videos into required formates.
4. IAM can also be implemented to set up user permission, so that only authorised personnel can perform the task of view, edit, transform and publish the video, information of permissioned personnel. 
5. Social media accounts can be stored via dynamo db. Say if there will be 20 users using this servce.
6. An elastic load balancer can be implemented to on top of ec2 in order to make the process more efficient while multiple users are using the service simultaneously. 
7. Lambda function can be implemented to process the user demand after video are transfromed, the demand of user can be obtained while videos are transforming (the 45min to 1 hour time) and inform users when the process is done, so that users do not have to wait until the tranformation procees to finish to perform their next step (i.e. publish to each social media platforms)

#### **1.2  (10 points) The company currently creates on average 50 videos per month and it’s not likely to increase the demand of clients for the next couple of years. Take also into account that there are less than 20 people that will be using the system. Discuss how you could change the previous solution using now a full serverless architecture and what benefits and disadvantages would have this new architecture over the previous architecture using EC2 instances.**

Lambda pros and cons:
https://www.linkedin.com/pulse/pros-cons-aws-Lambda-ashish-saxena/

1. The ec2 approach may be not worth the value as the monthly average of 50 videos with small potential of increasing in the futrue, and less than 20 people will use the system. 
2. we suggest replacing the ec2 approach with Lambda to reduce the cost, since Lambda can do almost everything that ec2 can, and the company only needs to pay per execution, which is a lot cheaper than ec2 in this senario. And we can remove ELB as well since Lambda are elastic by nature.
3. But Lambda has computational restrictions and has less control over the application, which need to be considered before replacing.


## 2. (20 points)
A professor in Computer Science at UWA has data from all labs, mid-term exam and final exam marks for the last two years of every student in csv format. He first noticed that in previous years those students that did very well in the labs and mid-term exam for a particular unit got at least 70% marks in the final exam. This year, the professor only has access to the labs and mid-term exam marks in csv format. However, he thinks he can predict the outcome of the final exam for students before marking the final exam.
#### **2.1  (10  points)  How would you use AWS technologies to  prove  (or disprove)  his theory and  help the professor predicting the marks for the current students this year?**

AWS sagemaker can be implement to train models based on the given data (labs and mid-term markd of this year) to predict the final exam mark. Model to use including linear regression, regression tree, random forest or artifitial neural network.

steps to build the model via sakemaker:
1. collect the data and formulate the problem (use given data to predict exam mark)
2. clean and tranform the data (labs and mst marks)
3. split the data in to training and test set 
4.  train the selected model using training set.
5. evaluate the trained model (run on test data, or use metric to validate, validation metrics including MAE, RMSE and MSE since this have to be regression model )
6. check if the result suggested by the model supports the professor's theory or not.

#### **2.2 (10 points) What approach would you use to assess the data models and help with the data analysis of the results?**
1. Selecting evaluation metrics to assess regression models (e.g. MAE, RMSE，MSE),
2. Comparing the results of training and testing set under each evaluation metric to see if any overfitting issues exist, 
3. Comparing the results of the selected model and a single variable model under each evaluation metric to see if the selected model has a good performance.


## 3. (10 points)
A  software  developer  wants  to  create  a  Drobox-like  application  for  Photographers  where  they  could seamlessly upload pictures from a local machine to the cloud and synchronise the data across multiple devices (Computer, Mobile Phones, etc.) for authenticated users. For every image uploaded by the users, she wants to save the metadata related to the file. Given the files uploaded by users are very important, she wants to allow restoring such files even if users delete the images on purpose. In addition, the software developer wants to automatically create labels for the uploaded images so they can perform searches of images based on the generated labels.
#### **3 Describe your approach using AWS technologies to create that application.**

1. using EC2 instances to host web services that provides REST API for processing user requests and interacting with other system components. 
2. using S3 buckets to store images uploaded by users.
3. using dynamoDB to save the metadata of the image.
4. using IAM to give permission to specific users, whose authorised information is stored using dynanmoDB,
5. using rekognition or implementing multi-class classification algorithms using sagemaker to retrieve the labels of each photo.
6. using DevOps services such as fabric to automate the process of software installation and configuration.
 
## 4. (20 points)
A MedTech company in Perth has created a novel algorithm for detecting heart diseases from X-rays and CT scans  (medical  images)  using  machine  learning  and  computer  vision.  The  company  now  wants  to commercialise it as a Software-as-a-service (SaaS) product. Initially, this product should allow authorised radiologist working at the Royal Perth Hospital to upload such images. Then, once the algorithm can process the image (it could take a couple of minutes) it should retrieve the prediction.   The solution should be scalable so it can be used in other hospitals in the future.
#### **4 Give 10 recommendations to the company on how they could use AWS to create this platform. Provide your answer as a list of bullet points.**
 
1. Applying serverless architecture AWS Lambda to reduce the cost and facilitate the need of developing SaaS product,
2. Implementing autoscaling to improve the efficiency.
3. Using S3 bucket to store the image files.
4. Using dynamoDB to store the metadata of each image.
5. Using IAM to control access and permissions of users.
6. Using algorithms in sagemaker or rekognition to process the image.
7. Using the version control tool such as AWS CodeCommit to maintain changes in the source code for disaster recovery.
8. Using AWS CodePipeline to perform Continuous Integration/Continuous Delivery (CI & CD) service for updating code.
9.  Using AWS CodeBuild to compile source code, run tests, and produce software packages. 
10. Using AWS CodeDeploy to test and deploy new code.
11. Using AWS Chef to manage machines. stacks, layers and applications can be established. 
12. Hiring IT experts to develop, maintain, and update the service.






## 5. (20 points)
You are a consultant who has been asked to write a report for a rapidly growing pet food company (PFC), based in Perth who would like to upgrade their systems to cope with the increasing global demand for their products. The company has rented space in a data centre for their systems that are a mix of Windows and Linux Servers, networking and firewall equipment and a range of storage devices (SANs, NAS, disk drives in servers). The company uses a range of software that they have purchased over the years that run on these machines. The functionality covered is everything from finance, sales and manufacturing to online product sales through their website.  PFC  have  received venture  capital funding and want to  expand  into  new markets, especially Asia and China in particular. To do this, they will need to be able to use modern systems that scale and operate at global scale.
#### **5 Provide 5 pros and 5 cons of moving infrastructure from being on-premises to cloud based. Consider this in the context of global expansion and resilience. Provide your answer as a list of bullet points.**

pros 
1. as compared to data centres, cloud-based systems have higher scalability.
2. cost of using and maintaining a cloud based infrastructure are much cheaper than  data centres 
3. given that cloud are distributed aboud the globe, services can operate faster in Asia and China for a Australian based company if using cloud rather than data centre 
4. cloud and more resource-saving compare to data centres since it scales according to demand
5. cloud are easy to recover from incidents and easy to back up as compared to data centres


cons:
1. local government regulations may not support cloud based technologies (China donot support their own data stored on clouds that are based outside of China)
2. data centre are more secure than using clouds, given that data centre are fully owned by the company, and therefore data will be stored fully by the company, whereas for cloud based, data have to upload to clouds, where data are exposed to leakage, especially when using dockers.
3. change on to cloud based is challenging for accounting departments
4. data centres can achieve more customised services compared to cloud, given that data centres are fully owned by the company, whereas cloud based can only use the services provided by the cloud.
5. once a cloud service is chosen (e.g. google cloud or AWS) it is hard to shift to other cloud or their own databse if the company find the services provided is unsatiisfying

