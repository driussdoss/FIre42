# - find Amazon2 id
# - create instance with user date script
import boto3

REGION = "us-east-1"
USER_DATE_PATH_FILE = "/home/dss/DevOps/Fire42/day_1/boto3-inst-am2.sh"
try:
    with open(USER_DATE_PATH_FILE, "r") as user_data_file:
        user_data_script = user_data_file.read()
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

    ami_id = str(latest_image["ImageId"])
    print(f"The latest Amazon Linux 2 AMI in {REGION} is: {ami_id}")
    print(type(ami_id))
except Exception as e:
    print(f"An error occurred: {e}")
try:
    ec2_client = boto3.client("ec2")
    response = ec2_client.run_instances(
        ImageId=ami_id,
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1,
        KeyName="vprofile",
        UserData=user_data_script,
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {"Key": "Name", "Value": "boto3-instance"},
                ],
            },
        ],
    )
    instance_id = response["Instances"][0]["InstanceId"]
    print(f"Successfully launched instance EC2, instance id: {instance_id}")
except Exception as e:
    print(f"An error occurred: {e}")
