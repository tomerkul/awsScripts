import boto3
import argparse

# Create a Boto3 EC2 resource object
ec2_resource = boto3.resource('ec2')

# Parse command line arguments
parser = argparse.ArgumentParser(description='Manage EC2 instances.')
parser.add_argument('--action', choices=['stop', 'start', 'destroy'], help='Specify the action to perform on instances.')
args = parser.parse_args()

# Retrieve all instances
instances = ec2_resource.instances.all()

# Stop, start, or destroy instances based on the action
for instance in instances:
    if args.action == 'stop':
        instance.stop()
        print(f"Stopping instance: {instance.id}")
    elif args.action == 'start':
        instance.start()
        print(f"Starting instance: {instance.id}")
    elif args.action == 'destroy':
        confirmation = input(f"Are you sure you want to destroy instance {instance.id}? (y/n): ")
        if confirmation.lower() == 'y':
            instance.terminate()
            print(f"Destroying instance: {instance.id}")
        else:
            print(f"Skipping destruction of instance: {instance.id}")
