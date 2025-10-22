import boto3

REGION = "us-east-1"

try:
    ec2_client = boto3.client("ec2", region_name=REGION)

    # Use filters to narrow down the search
    images = ec2_client.describe_images(
        Filters=[
            {
                "Name": "name",
                "Values": [
                    "amzn2-ami-hvm-*-x86_64-gp2"
                ],  # Wildcard to find the latest version
            },
            {"Name": "state", "Values": ["available"]},
        ],
        Owners=["amazon"],  # Find official Amazon AMIs
    )

    # Sort images by creation date to find the most recent one
    latest_image = sorted(
        images["Images"], key=lambda x: x["CreationDate"], reverse=True
    )[0]

    ami_id = latest_image["ImageId"]
    print(f"The latest Amazon Linux 2 AMI in {REGION} is: {ami_id}")

except Exception as e:
    print(f"An error occurred: {e}")
