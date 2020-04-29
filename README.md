# ECS-AutoDeployment
Our main scope of this auto deployment is whenever new images is updated in ECR, Deployment should trgigger in ECS Service without downtime and here is the process of ECS Auto Deployment

"Zero Downtime Deployment with ECS, CloudWatch Event and Lambda"

Create CloudWatch Event "Service Name--ECR" and "Event Type--AWS API Call via CloudTrail" then add Specific operration--"PutImage" means this event will trigger whenever new Image is uploaded to ECR 

Create Lambda Function to update the service which is below mention python script
