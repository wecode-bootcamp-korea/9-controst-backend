import bcrypt
import names
import json
import jwt

from django.http import JsonResponse, HttpResponse
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.views import View

from trost.settings import SECRET_KEY, HASH_KEY
from partner.models import (
        Counselor,
        Product
)
from .models import (
        History,
        User
)
from .models import User


class SignUpView(View):
    def post(self, request):
        data=json.loads(request.body)
        # regex of email address validation
        email_validator = RegexValidator(regex = '^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$')
        # regex of password validation
        psw_validator = RegexValidator(regex='^.*(?=^.{6,14}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&*?()_~]).*$')

        try:
            email_validator(data['email'])
            if User.objects.filter(email=data['email']).exists():
                return HttpResponse(status=400)
            psw_validator(data['password'])
            enc_pw=bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            final_nickname = data['nickname']
            if not data['nickname']:
                # random nickname generator
                final_nickname = names.get_first_name()
            # saving data
            User(
                email    = data['email'],
                password = enc_pw.decode('utf-8'),
                nickname = final_nickname,
            ).save()
        except ValidationError:
            return HttpResponse(status= 400)
        else:
            return JsonResponse({'message':'SUCCESS'}, status=200)

# the button of checking email duplication
class EmailCheckView(View):
    def post(self, request):
        data=json.loads(request.body)
        if User.objects.filter(email=data['email']).exists():
            return HttpResponse(status= 400)
        else:
            return HttpResponse(status= 200)

# the button of checking nickname duplication
class NicknameCheckView(View):
    def post(self, request):
        data=json.loads(request.body)
        if User.objects.filter(nickname=data['nickname']).exists():
            return HttpResponse(status= 400)
        else:
            return HttpResponse(status= 200)

    def get(self, request):
        return HttpResponse(status=200)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email=data['email']).exists():
                user_info = User.objects.get(email=data['email'])
                # password decrypting
                if bcrypt.checkpw(data['password'].encode('utf-8'), user_info.password.encode('utf-8')):
                    token=jwt.encode({"email":user_info.email}, SECRET_KEY, algorithm=HASH_KEY).decode('utf-8')
                    return JsonResponse({"token":token}, status = 200)
                return HttpResponse(status = 401)
            return HttpResponse(status = 400)
        except KeyError:
            return jsonResponse({'message': 'Invalid_KEY'})

    def get(self, request):
        return HttpResponse(status=200)

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

class HistoryView(View):
    @login_decorator
    def get(self, request):
        account = request.user
        user_info = History.objects.filter(user__email = account.email).select_related('counselor').select_related('product')
        history_list = [
                {
                "counselor_name"    : info.counselor.name,
                "counselor_level"   : info.counselor.level.name,
                "profile_image_url" : info.counselor.profile_image_url,
                "product_kind"      : info.product.kind.name,
                "product_duration"  : info.product.duration.name,
                "product_price"     : info.product.price,
                "counsel_date"      : info.created_at
                } for info in user_info
                ]
        return JsonResponse({"user_history":history_list}, status=200)
