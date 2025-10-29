#!/usr/bin/env python3

import boto3


#create S3-bucket

s3 = boto3.client("s3")
s3.create_bucket(Bucket="dss-boto3-first-bucket")

