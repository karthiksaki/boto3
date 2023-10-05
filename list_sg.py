import boto3
from botocore.exceptions import ClientError
from pprint import pprint
aws_console = boto3.Session(profile_name="default")
ec2 = aws_console.client('ec2')
response = ec2.describe_security_groups()
responses =  response['SecurityGroups']
# pprint(responses)
# pprint(response['SecurityGroups'])
for group in responses:
    group_name = group['GroupName']
    group_id = group['GroupId']
    print(f"Security Group Name: {group_name}, Security_Group_id::{group_id}")
