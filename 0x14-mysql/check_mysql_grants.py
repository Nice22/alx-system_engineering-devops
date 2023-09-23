#!/usr/bin/python3
"""
This script will verify that a student has granted the checker SELECT access
to their databases on their web-01 and web-02 servers.
"""
import sys

from fabric import Connection
from io import StringIO
from paramiko import RSAKey


host = sys.argv[1]
user = sys.argv[2]
rsa_key_file = sys.argv[3]

rsa_key = RSAKey.from_private_key(open(rsa_key_file))
output = StringIO()

with Connection(host, user=user, connect_kwargs={"pkey": rsa_key}) as c:
    c.run("mysql -uholberton_user -pprojectcorrection280hbtn -e 'show grants for \'holberton_user\'@\'localhost\'' 2>&1", shell="/bin/bash", out_stream=output, warn=False)
    output = output.getvalue().split('\n')[2:]
    for item in output:
        grants = item.split()
        if ('SELECT' in grants or 'ALL' in grants) and ('*.*' in grants or '`tyrell_corp`.*' in grants or '`tyrell_corp`.`nexus6`' in grants):
            print('Correct grants given', end='')
            exit(0)

print('\n'.join(output))
