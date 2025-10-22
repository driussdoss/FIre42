import boto3

ins_desc = boto3.client("ec2")

inst_show = ins_desc.describe_instances()
print("Instances:", inst_show["Reservations"])
