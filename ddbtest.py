#!/usr/bin/env python3

from configparser import ConfigParser, NoSectionError, NoOptionError
import boto3
import boto3.session
from boto3.dynamodb.conditions import Key, Attr
import sys

parser = ConfigParser()
parser.read('config.ini')

try:
    region_name = parser.get('main', 'region_name')
    table_name = parser.get('main', 'table')
    access_key_id = parser.get('main', 'access_key_id')
    secret_access_key = parser.get('main', 'secret_access_key')
except (NoSectionError, NoOptionError) as err:
    print(f"Error reading config.ini: {err}")
    sys.exit(1)

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

table.put_item(
   Item={
        'userid': 'userid#0',
        'bkmkid': 'bkmkid#3',
        'url': 'https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html',
    }
)

response = table.query(
    KeyConditionExpression=Key('userid').eq('userid#0')
)
items = response['Items']
print(items)

table.delete_item(
    Key={
        'userid': 'userid#0',
        'bkmkid': 'bkmkid#3'
    }
)

response = table.query(
    KeyConditionExpression=Key('userid').eq('userid#0')
)
items = response['Items']
print(items)
