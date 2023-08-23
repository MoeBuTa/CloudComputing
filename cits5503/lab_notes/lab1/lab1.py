import boto3
import pandas as pd
from tabulate import tabulate

ec2=boto3.client('ec2')
response=ec2.describe_regions()
region_list = pd.DataFrame(response['Regions'], columns=['Endpoint', 'RegionName'])
print(tabulate(region_list,headers='keys', tablefmt='psql',   showindex=False))



