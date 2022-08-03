import logging

from cliff.command import Command

from boto3.dynamodb.conditions import Key, Attr

class List(Command):
    "list bookmarks."

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        response = self.app.ddb_con.table.query(
            KeyConditionExpression=Key('userid').eq('userid#0')
        )
        for item in response['Items']:
            self.app.stdout.write('[' + item['bkmkid'] + ']')
            if 'url' in item:
                self.app.stdout.write(' ' + item['url'])
            self.app.stdout.write('\n')

