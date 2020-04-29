from __future__ import print_function
from botocore.vendored import requests
from boto3 import session, client
import boto3
import json
import os

region = "name"
client = boto3.client('ecs', region_name=region)


response = client.list_task_definitions(familyPrefix= 'service-name', status='ACTIVE')

def lambda_handler(event, context):
    response = client.register_task_definition(
    family='service-name',
    taskRoleArn='role arn',
    executionRoleArn='role arn',
    networkMode='awsvpc',
    requiresCompatibilities=[
            'FARGATE',
        ],
    cpu='1024',
    memory='2048',
    containerDefinitions=[
        {
            'name': 'mercury',
            'image': 'image uri',
            'cpu': 1024,
            'memory': 2048,
            'portMappings': [
                {
                    'containerPort': 8000,
                    'hostPort': 8000,
                    'protocol': 'tcp'
                },
            ],
            'essential': True|False,
            
            'environment': [
                {
                    'name': 'SECRET_KEY',
                    'value': os.environ["SECRET_KEY"],
                },
                {
                    'name': 'URL',
                    'value': os.environ["URL"],
                },
                {
                    'name': 'ENVIRONMENT',
                    'value': os.environ["ENV"],
                },
            ],
            "logConfiguration": {
              "logDriver": "awslogs",
              "options": {
                "awslogs-group" : "/ecs/mercury",
                "awslogs-region": "name",
               "awslogs-stream-prefix": "ecs"
          }
        },
        },
      ],
    )
    taskDefinitionRev = response['taskDefinition']['family'] + ':' + str(response['taskDefinition']['revision'])


    response = client.update_service(
        cluster='cluster',
        service='service-name',
        desiredCount=1,
        taskDefinition=taskDefinitionRev,
        deploymentConfiguration={
            'maximumPercent': 200,
            'minimumHealthyPercent': 100
        },
        forceNewDeployment=True
    )
    #pprint.pprint(response)
    print("service updated")