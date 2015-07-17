import os

PROCESSES = 4
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
TEMP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'temp'))

CONNECTIONS = [
   #['switch name', 'switch address', 'username', 'password'],
]

COMMANDS = [
    ['portlogdump', 'portlogdump'],
]

ARGUMENTS = []
for connection in CONNECTIONS:
    ARGUMENTS.append(connection + [COMMANDS])
