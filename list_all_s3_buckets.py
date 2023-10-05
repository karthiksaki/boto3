import boto3
import datetime
from pprint import pprint

aws_console = boto3.Session(profile_name="default")
Buckets_list = aws_console.resource('s3')
response =  Buckets_list.list_buckets()
pprint(response)
# print("Existing Buckets::")
#
# for bucket in response['Buckets']:
#     print(f'Bucket Name: {bucket["Name"]}')


# for i in response['Buckets']:
#     print(f'{owner['DisplayName']}')

