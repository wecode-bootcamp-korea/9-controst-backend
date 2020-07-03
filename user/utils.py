import jwt
import json

from django.http import JsonResponse

from trost.settings import SECRET_KEY, HASH_KEY
from user.models import User, History

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token = request.headers.get('Authorization', None)
            payload = jwt.decode(token, SECRET_KEY, algorithm=HASH_KEY)
            user_mail = User.objects.get(email=payload['email'])
            request.user = user_mail
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'Invalid_token' }, status=400)
        except Account.DoesNotExist:
            return JsonResponse({'message' : 'Invalid_user'}, status=400)
        return func(self, request, *args, **kwargs)
    return wrapper
