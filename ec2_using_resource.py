import boto3
from pprint import pprint
aws_console = boto3.Session(profile_name="default")
ec2_resource = aws_console.resource("ec2")
ec2_client = aws_console.client('ec2')
for i in ec2_resource.instances.all():
    print(i.id,i.state['Name'])
    print(f"Availability Zone: {i.placement['AvailabilityZone']}")  # Access the 'AvailabilityZone' attribute of the 'placement' dictionary
