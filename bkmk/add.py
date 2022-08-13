import logging

from cliff.command import Command

from boto3.dynamodb.conditions import Key, Attr
import ulid

class Add(Command):
    "add a bookmark."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Add, self).get_parser(prog_name)
        parser.add_argument('-d', '--desc', help='bookmark description', nargs=1)
        parser.add_argument('url', help='bookmark url', nargs=1)
        return parser

    def take_action(self, parsed_args):
        bkmkid = "bkmkid#" + ulid.new().str

        url = parsed_args.url[0]

        item = {
                'userid': 'userid#0',
                'bkmkid': bkmkid,
                'url': url,
        }

        if parsed_args.desc:
            item['desc'] = parsed_args.desc[0]

        self.app.ddb_con.table.put_item(Item=item)


