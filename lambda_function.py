import boto3
client= boto3.client('ec2')
stsclient = boto3.client('sts')


def lambda_handler(event, context):
    identity = stsclient.get_caller_identity()
    account_id = identity["Account"]
    TAG_VALUE = "ansible-server"
    USERDATA = "ansible_userdata.txt"
    with open(USERDATA, 'r') as file:
        userdata_context = file.read()
        
    response = client.run_instances(
        ImageId = "ami-08928044842b396f0",
        KeyName = "abetest",
        InstanceType = "t2.micro",
        MaxCount = 1,
        MinCount = 1,
        IamInstanceProfile = {"Arn": "arn:aws:iam::" + account_id + ":instance-profile/ansible-server"},
        NetworkInterfaces = [{
            "AssociatePublicIpAddress": True,
            "DeviceIndex": 0,
            "Groups": ["sg-09ffe94af8dfdb2de"],
            "SubnetId": "subnet-0f94a01bdaacf8038"
        }],
        TagSpecifications = [
            {
                "ResourceType": "instance",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": TAG_VALUE
                    },
                ]
            },
        ],
        UserData = userdata_context)
