#!/usr/bin/env python3


import boto3, paramiko

#get default security group ID
try:
aws_ec2_client = boto3.client("ec2")
aws_ec2_sg = aws_ec2_client.describe_security_groups()

for aws_sg in aws_ec2_sg['SecurityGroups']:
    if aws_sg['GroupName'] == 'default':
        AWS_SG_def = aws_sg['GroupID']


#run instance

awslinux = boto3.run_instance(
        ImageId = "",
        InstanceType = "t2.micro",
        MinCount=1,
        MaxCount=1,
        KeyName = "vprofile",
        SecurityGroupId = AWS_SG_def
        )
except Exep
