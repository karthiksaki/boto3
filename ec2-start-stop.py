import boto3
from botocore.exceptions import ClientError
from pprint import pprint
aws_console = boto3.Session(profile_name="default")
ec2_resource = aws_console.resource("ec2")

instance_id = input("Enter the Instance_id for which you want to stop the Instances;; ")

karthik = ec2_resource.Instance(instance_id)
# pprint(karthik)
## Next two lines of code is for stopping the instance,waiter functions are used for waiting
# karthik.stop()
# karthik.wait_until_stopped()
try:
## Next two lines of code is for starting the instance,waiter functions are used for waiting
    karthik.start()
    karthik.wait_until_running()
    print("Instance {} has been started.".format(instance_id))

except ClientError as e:
    print("An error occurred:", str(e))

except Exception as e:
    print("An unexpected error occurred:", str(e))
