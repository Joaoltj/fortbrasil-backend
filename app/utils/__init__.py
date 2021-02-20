from flask import make_response
http_status = {
    'OK':200,
    'CREATED': 201,
    'NOT_FOUND':404,
    'BAD_REQUEST':400,
    'SERVER_ERROR':500
}


def response_bad_request(error):
    return make_response({'error':error},http_status.get('BAD_REQUEST'))

def response_server_error(error):
    return make_response({
        'error':error
    },http_status.get('SERVER_ERROR'))

def response_created(data):
    return make_response({
        'data':data
    },http_status.get('CREATED'))

def response_ok(data):
    return make_response({
        'data':data
    },http_status.get('OK'))


def response_not_found(message):
    return make_response({
        'error': message
    }, http_status.get('NOT_FOUND'))