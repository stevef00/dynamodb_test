import logging

from cliff.command import Command

from boto3.dynamodb.conditions import Key, Attr
import ulid

class Rm(Command):
    "remove a bookmark."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Rm, self).get_parser(prog_name)
        parser.add_argument('bkmkid', help='bookmark id', nargs=1)
        return parser

    def take_action(self, parsed_args):
        bkmkid = parsed_args.bkmkid[0]

        self.app.ddb_con.table.delete_item(
            Key={
                'userid': 'userid#0',
                'bkmkid': bkmkid,
            }
        )
