import boto3
import time

aws_mag_con = boto3.Session(profile_name="default")
ec2 = aws_mag_con.client('ec2')

# List running instances
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
instances = response['Reservations']

for reservation in instances:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        
        # Create an AMI
        image_name = f"AMI for instance {instance_id}"
        ami_response = ec2.create_image(InstanceId=instance_id, Name=image_name, NoReboot=True)
        ami_id = ami_response['ImageId']
        
        print(f"AMI created with ID: {ami_id}")
        
        # # Create snapshots of EBS volumes
        # for block_device in instance['BlockDeviceMappings']:
        #     volume_id = block_device['Ebs']['VolumeId']
        #     snapshot_response = ec2.create_snapshot(VolumeId=volume_id, Description=f"Snapshot for instance {instance_id}")
        #     snapshot_id = snapshot_response['SnapshotId']
            
        #     print(f"Snapshot created with ID: {snapshot_id} for Volume: {volume_id}")
