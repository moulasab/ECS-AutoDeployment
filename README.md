# ECS-AutoDeployment
Our main scope of this auto deployment is whenever new images is updated in ECR, Deployment should trgigger in ECS Service without downtime and here is the process of ECS Auto Deployment

We can Implement ECS Auto deplotment with these two process 
"Zero Downtime Deployment with ECS, CloudWatch Event and Lambda"
1) Create CloudWatch Event by selecting these details 
   "Service Name--ECR" and 
   "Event Type--AWS API Call via CloudTrail" then add 
   Specific operration--"PutImage" means this event will trigger whenever new Image is uploaded to ECR 
2) Select Lambda Fucntion name from dropdown in Add Target in above Event creation
2) Create Lambda Function to update the service which is below mention python script

Note:Add all sensitive data or database details or urls in Lambda Environment variables

This is another way to implement this auto deployment process 

CloudTrail, CloudWatch Log Group, CloudWatch Alarm, SNS and Lambda and in this process there is time delay(5min to 15min) in deployment due to CloudTrail event to Cloudwatch log groups 

1) First we have create CloudTrail and specify logs group while creating
2) Goto CloudWatch Log Groups and select the group name then create metric filter "{ ($.eventSource = ecr.amazonaws.com) && ($.eventName = PutImage) && ($.requestParameters.repositoryName = “<YourRepoName>”) && ($.errorCode NOT EXISTS) }"
3) Create alarm using this metric 
4) Create SNS topic then assign to above alarm action
5) Now create Lambda function to update the ECS Service and this Lambda should trigger from the above SNS 
