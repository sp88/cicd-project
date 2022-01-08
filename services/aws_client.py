import os
import boto3

REGION_NAME = "ap-south-1"
_instance_id = None
_public_ip = None

def create_key_pair():
    ec2_client = boto3.client("ec2", region_name=REGION_NAME)
    key_pair = ec2_client.create_key_pair(KeyName="ec2-key-pair")

    private_key = key_pair["KeyMaterial"]

    # write private key to file with 400 permissions
    with os.fdopen(os.open("./services/aa.pem", os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle: #  "./services/aws_ec2_key.pem"
        handle.write(private_key)


def create_instance():
    ec2_client = boto3.client("ec2", region_name=REGION_NAME)
    instances = ec2_client.run_instances(
        ImageId="ami-02f8fc920ae787f77",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ec2-key-pair"
    )
    _instance_id = instances["Instances"][0]["InstanceId"]
    print(_instance_id)


def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name=REGION_NAME)
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            return instance.get("PublicIpAddress")



# create_key_pair()
# create_instance()
get_public_ip("i-0e96098a8f2f01e5d")
