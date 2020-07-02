from django.http import JsonResponse, HttpResponse
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from partner.models import Counselor, Product
from .models import History, User
from trost.settings import SECRET_KEY
from django.views import View
from .models import User
import bcrypt
import names
import json
import jwt

class SignUpView(View):
    def post(self, request):
        data=json.loads(request.body)
        # regex of email address validation
        email_validator = RegexValidator(regex = '^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$')
        # regex of password validation
        psw_validator = RegexValidator(regex='^.*(?=^.{6,14}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&*?()_~]).*$')

        # the button of signup
        if 'email' in data.keys() and 'password' in data.keys() and 'nickname' in data.keys():
            # email address validation
            try:
                email_validator(data['email'])
            except ValidationError:
                return JsonResponse({'message':'Invalid email'}, status= 400)
            # check email duplication
            else:
                if User.objects.filter(email=data['email']).exists():
                    return JsonResponse({'message':'이미 사용 중인 이메일 입니다.'}, status=400)
                # password validation
                else:
                    try:
                        psw_validator(data['password'])
                    except ValidationError:
                        return JsonResponse({'message':'Invalid password'}, status= 400)
                    else:
                        enc_pw=bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

                        # random nickname generator
                        if data['nickname'] != '':
                            final_nickname = data['nickname']
                        else:
                            final_nickname = names.get_first_name()

                        # saving data
                        User(
                            email    = data['email'],
                            password = enc_pw.decode('utf-8'),
                            nickname = final_nickname,
                        ).save()
                        return JsonResponse({'message':'SUCCESS'}, status=200)

        # the button of checking email duplication
        elif 'email' in data.keys() and 'password' not in data.keys() and 'nickname' not in data.keys():
            try:
                email_validator(data['email'])
            except ValidationError:
                return JsonResponse({'message':'Invalid email'}, status= 400)
            else:
                if User.objects.filter(email=data['email']).exists():
                    return JsonResponse({'message':'이미 사용 중인 이메일 입니다.'}, status= 400)
                else:
                    return JsonResponse({'message':'사용 가능한 이메일 입니다.'}, status= 200)

        # the button of checking nickname duplication
        elif 'email' not in data.keys() and 'password' not in data.keys() and 'nickname' in data.keys():
            if User.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({'message':'이미 사용 중인 닉네임입니다.'}, status= 400)
            else:
                return JsonResponse({'message':'사용 가능한 닉네임입니다.'}, status= 200)

    def get(self, request):
        return JsonResponse({"message":"success"}, status=200)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email=data['email']).exists():
                user_info = User.objects.get(email=data['email'])
                # password decrypting
                if bcrypt.checkpw(data['password'].encode('utf-8'), user_info.password.encode('utf-8')):
                    token=jwt.encode({"email":user_info.email}, SECRET_KEY, algorithm='HS256').decode('utf-8')
                    return JsonResponse({"token":token}, status = 200)
                return JsonResponse({"message":"계정 또는 비밀번호가 일치하지 않습니다."}, status = 401)
            return JsonResponse({'message':'계정 또는 비밀번호가 일치하지 않습니다.'}, status = 400)
        except KeyError:
            return jsonResponse({'message': 'Invalid_KEY'})

    def get(self, request):
        return JsonResponse({"message":"success"}, status=200)

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token = request.headers.get('Authorization', None)
            payload = jwt.decode(token, SECRET_KEY, algorithm='HS256')
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
        user_info = History.objects.filter(user__email = account.email)
        history_list = []
        for i in range(len(user_info)):
            history_list.append(
                {
                "counselor_name":user_info[i].counselor.name,
                "counselor_level":user_info[i].counselor.level.name,
                "profile_image_url":user_info[i].counselor.profile_image_url,
                "product_kind":user_info[i].product.kind.name,
                "product_duration":user_info[i].product.duration.name,
                "product_price":user_info[i].product.price,
                "counsel_date":user_info[i].created_at
                })
        return JsonResponse({"user_history":history_list}, status=200)
