import sys
from gvm.connections import TLSConnection
from gvm.protocols.latest import Gmp
from gvm.xml import pretty_print
from gvm.transforms import EtreeCheckCommandTransform
from gvm.errors import GvmError

connection = TLSConnection(hostname='100.74.219.96', port=9390)
transform = EtreeCheckCommandTransform()

username = 'Team'
password= 'UsK]+m1KXNAyTT?fpWjS'

try:
    tasks = []

    with Gmp(connection=connection, transform=transform) as gmp:
        gmp.authenticate(username, password)

        tasks = gmp.get_tasks(filter_string='name~weekly')

        for task in tasks.xpath('task'):
            print(task.find('name').text)

except GvmError as e:
    print('An error occurred', e, file=sys.stderr)



