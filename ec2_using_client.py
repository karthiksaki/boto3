import boto3
from pprint import pprint
aws_console = boto3.Session(profile_name="default")
ec2_client = aws_console.client('ec2')
karthik = ec2_client.describe_instances()['Reservations']
# pprint(karthik)
for abc in karthik:
    for xyz in abc['Instances']:
        print(f"AMI_ID used is {xyz['ImageId']}")
        print(xyz['InstanceId'])
