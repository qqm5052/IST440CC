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
    'message': {
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

message_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'message': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
    },
    'numberOfTimes':{
        'type': 'integer',
    },
    'timestamp': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30,
        'required': True,
        'unique': False,
    },
    'sent': {
        'type': 'boolean',
        'required': True,
        'unique': False,
    }
}
messages = {
    'item_title': 'messages',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    # most global settings can be overridden at resource level
    'resource_methods': ['GET','POST','DELETE'],
    'schema': message_schema
}

DOMAIN = {
    'status': status,
    'messages': messages
}