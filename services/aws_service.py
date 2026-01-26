import boto3
from datetime import datetime, timezone, timedelta
import pytz # type: ignore

def get_connection(service_name):
    return boto3.client(service_name, region_name="us-east-1")


def create_key_pair(ec2, request):
    data = ec2.create_key_pair(
        KeyName=request.key_name,
        KeyType='rsa',
        KeyFormat='pem'
    )

    return data

def generate_key_pem_file(request, key_pair):
    with open(f"{request.key_name}.pem", "w") as file:
        file.writelines(key_pair['KeyMaterial'])




def get_bucket_info():

    """
        This API gets the s3 buckets
    """
    s3_client = get_connection("s3")

    buckets = s3_client.list_buckets()["Buckets"]

    current_datetime = datetime.now(timezone.utc).astimezone()
    print("current time: ",current_datetime)

    old_bukets = []
    new_buckets = []

    for bucket in buckets:
        bucket_name = bucket["Name"]
        
        creation_date = bucket["CreationDate"]
        days_ago_90 = current_datetime - timedelta(days=90)

        if creation_date < days_ago_90:
            old_bukets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)



    return {
        "Total Buckets": len(buckets),
        "New Buckets": len(new_buckets),
        "Old Buckets":old_bukets,
        "New Buckets Names": new_buckets,
        "Old Buckets Name": old_bukets

    }


def get_ec2_info():


    """
        This API gets the Ec2 instance Details.
    """
    ec2 = get_connection("ec2")
    l = []
    res = ec2.describe_instances()
    #print(res["Reservations"])
    for i in res["Reservations"]:

        dict = {
            "Instance Id " : i['Instances'][0]['InstanceId'] ,
            "Instance Type" : i['Instances'][0]['InstanceType'],
            "Image Id" : i['Instances'][0]['ImageId'],
            "Root Device Name" : i['Instances'][0]['RootDeviceName'],
            "Root Device Type" : i['Instances'][0]['RootDeviceType'],
            "Security Group" : i['Instances'][0]['SecurityGroups'],
            "Monitoring State" : i['Instances'][0]['State'],
            "Tags" : i['Instances'][0]['Tags']
        }
        l.append(dict)
    return l


def get_iam_users():
    """
        This API gets the IAM Users on the Root Account.
    """
    iam = get_connection("iam")
    paginator = iam.get_paginator('list_users')
    l = []
    for res in paginator.paginate():
        for i in res["Users"]:
            user_dict = {
                "UserName": i["UserName"],
                "User Id": i["UserId"],
                "CreateDate": i["CreateDate"].strftime("%d-%m-%Y %H:%M:%S")
            }

            l.append(user_dict)

    return l



def create_ec2_instacne(request):
    """
        Creates a new EC2 instance using the provided parameters.
    """

    ec2 = get_connection("ec2")

    key_pair = create_key_pair(ec2, request)

    generate_key_pem_file(request, key_pair)

    
    response = ec2.run_instances(
    ImageId=request.ami_id,
    InstanceType=request.instance_type,
    KeyName=request.key_name,
    MinCount=request.min_count,
    MaxCount=request.max_count,
    TagSpecifications=[
        {
                "ResourceType": "instance",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": request.instance_name
                    }
                ]
            }
        ]
    )


    instance = response["Instances"][0]

    # Convert LaunchTime to IST
    ist = pytz.timezone("Asia/Kolkata")
    launch_time_ist = instance["LaunchTime"].astimezone(ist)

    return {
        "message": "EC2 instance created successfully",
        "instance_id": instance["InstanceId"],
        "launch_time": launch_time_ist.strftime("%d-%m-%Y %H:%M:%S IST")
    }




