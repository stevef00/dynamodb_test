#!/usr/bin/env python3

from configparser import ConfigParser
import boto3
import boto3.session

parser = ConfigParser()
parser.read('config.ini')

#with open("keys.txt", "r") as keys_file:
#    for line in keys_file:
#        line = line.rstrip()
#        if re.search("^#", line):
#            continue
#        elif re.search("^$", line):
#            continue

#        part = line.split('=')
#        if part[0] == 'USERNAME':
#            username = part[1]
#        elif part[0] == 'ACCESS_KEY_ID':
#            access_key_id = part[1]
#        elif part[0] == 'SECRET_ACCESS_KEY':
#            secret_access_key = part[1]
#        elif part[0] == 'TABLE_NAME':
#            table_name = part[1]
#        else:
#            print("ERROR")

region_name = parser.get('main', 'region_name')
table_name = parser.get('main', 'table')
access_key_id = parser.get('main', 'access_key_id')
secret_access_key = parser.get('main', 'secret_access_key')

# FIXME -- need to validate configuration

dynamodb = boto3.resource('dynamodb',
        aws_access_key_id = access_key_id,
        aws_secret_access_key = secret_access_key,
        region_name = region_name)

table = dynamodb.Table(table_name)

response = table.get_item(
        Key={
            'userid': 'userid#0',
            'bkmkid': 'bkmkid#2',
            }
        )
item = response['Item']
print(item)
