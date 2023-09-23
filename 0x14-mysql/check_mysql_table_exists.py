#!/usr/bin/python3
"""
Verifies that a student has created a database with a table that contains
at least one entry.
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
    c.run("mysql -uholberton_user -pprojectcorrection280hbtn -e 'use tyrell_corp; select * from nexus6' 2>&1", shell="/bin/bash", out_stream=output, warn=True)
    output = output.getvalue().split('\n')[2:]
    for item in output:
        if len(item) > 0:
            print('Table not empty', end='')
            exit(0)

print('\n'.join(output))
