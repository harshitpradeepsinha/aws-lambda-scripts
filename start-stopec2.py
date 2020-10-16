
import boto3
region = 'ec2-region'
instances = ['$ec2id','$moreids']
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances) #(change start stop as you like)
    print('stopped your instances: ' + str(instances))
