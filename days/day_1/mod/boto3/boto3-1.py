import boto3
from botocore.retries.adaptive import bucket

s3 = boto3.resource("s3")

s3.create_bucket(
    Bucket="uniqu-backet-fire42",
    CreateBucketConfiguration={"LocationConstraint": "us-east-2"},
)
print("S3 created")
