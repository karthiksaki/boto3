import boto3
from botocore.exceptions import NoCredentialsError

aws_mag_con = boto3.Session(profile_name="default")
ec2 = boto3.client('ec2')
s3_bucket_name = 'teknismart-sank'  # Change this to your S3 bucket name
s3_object_key = 'folder/index.html'  # Change this to the object key you want to delete


response = s3.delete_object(
    Bucket=s3_bucket_name,
    Key=s3_object_key
)

print(response)

