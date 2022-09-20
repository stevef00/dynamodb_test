#!/usr/bin/env python3

from cliff.app import App
from cliff.commandmanager import CommandManager

from configparser import ConfigParser, NoSectionError, NoOptionError
import boto3
import boto3.session
from boto3.dynamodb.conditions import Key, Attr
import os, sys

#response = table.get_item(
#        Key={
#            'userid': 'userid#0',
#            'bkmkid': 'bkmkid#2',
#            }
#        )
#item = response['Item']
#print(item)

#table.put_item(
#   Item={
#        'userid': 'userid#0',
#        'bkmkid': 'bkmkid#3',
#        'url': 'https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html',
#    }
#)

#response = table.query(
#    KeyConditionExpression=Key('userid').eq('userid#0')
#)
#items = response['Items']
#print(items)

#table.delete_item(
#    Key={
#        'userid': 'userid#0',
#        'bkmkid': 'bkmkid#3'
#    }
#)

#response = table.query(
#    KeyConditionExpression=Key('userid').eq('userid#0')
#)
#items = response['Items']
#print(items)

class DdbConn:
    def __init__(self, **kwargs):
        if kwargs.get('config_file'):
            parser = ConfigParser()
            parser.read(kwargs.get('config_file'))

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

        self.table = dynamodb.Table(table_name)

class BkmkApp(App):

    def __init__(self):
        super(BkmkApp, self).__init__(
            description='dynamodb demo app',
            version='0.1',
            command_manager=CommandManager('bkmk'),
            deferred_help=True,
            )

    def initialize_app(self, argv):
        user_config_dir = os.path.expanduser("~") + "/.config"
        user_config = user_config_dir + "/bkmk.ini"

        self.ddb_con = DdbConn(config_file=user_config)

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    myapp = BkmkApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
