MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'PuzzleStatus'
RESOURCE_METHODS = ['GET', 'PATCH', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

status_schema = {
    'teamname': {
        'type': 'string',
        'required': True,
    },
    'puzzlename': {
        'type': 'string',
        'required': True,
    },
    'status': {
        'type': 'string',
        'required': True,
    },
}
status = {
    'cache_control': 'max-age=10, must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'schema': status_schema
}

DOMAIN = {'status': status,}