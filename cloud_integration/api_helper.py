import json
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def handle_data_response_success(data):
    return ({'error': False,
             'msg': '',
             'data': data})


def handle_response_fail(message):
    return ({'error': True,
             'msg': message.get('msg'),
             'data': {}})


def check_permissions(func):
    def wrapper(self, *args, **kwargs):
        # Get access token from http header
        access_token = self.request.headers.get('Token')
        if access_token:
            access_token = access_token.strip()
        else:
            error_descrip = "No access token was provided in request!"
            return Response(handle_response_fail({'msg': error_descrip}))
        user_id = Token.objects.filter(key=access_token)[0].user
        if not user_id:
            return Response(handle_response_fail({'msg': 'Token was not correct'}))
        kwargs['user_id'] = user_id
        return func(self, *args, **kwargs)

    return wrapper