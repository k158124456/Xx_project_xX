from django.shortcuts import render
from django.views.generic import TemplateView
from sign_up.forms import SignupForm
from .models import UserList
from django.contrib.auth.models import User
# Create your views here.

#各入力欄での使用禁止文字\\はエスケープ文字でエスケープ文字をエスケープさせてる
unavailable_cha={'id':[" ","\\","<",">"],
                'mail':[" ","\\","<",">"],
                'password':[" ","\\","<",">"],}
useable_cha = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '1','2','3','4','5','6','7','8','9','0','_'
]

class SignUp(TemplateView):
    def __init__(self):
        self.params = {
            'form' : SignupForm(),
            'msg' : "",
            'debug' : "",
        }
    # メールアドレスに重複があるかどうか調べる関数
    def isin_mail(self, mail):
        user_mail = UserList.objects.filter(mail=mail)
        return str(user_mail) != "<QuerySet []>"

    #b IDがすでに登録があるかどうか調べる関数
    def isin_id(self, id):
        user_id = UserList.objects.filter(user_id=id)
        return str(user_id) != "<QuerySet []>"
        
    def inough_lengs(self, password, require=6):
        return len(password) < require
    
    #使用禁止文字判定id
    def unavailable_cha_id(self,id):
        for i in id:
            if i in unavailable_cha['id']:
                return True
        else:return False

    #使用可能文字判定id
    def available_cha_id(self,id):
        for i in id:
            if i in useable_cha:
                return False
        else:return True

    #使用禁止文字判定mail
    def unavailable_cha_mail(self,mail):
        for i in mail:
            if i in unavailable_cha['mail']:
                return True
        else:return False
    
    #使用禁止文字判定password
    def unavailable_cha_pass(self,password):
        for i in password:
            if i in unavailable_cha['password']:
                return True
        else:return False


    def need_chr_mail(self, mail):
        #self.params["debug"] = not ("@" in str(mail))
        return not ("@" in str(mail))


    def get(self, request):
        return render(request, 'sign_up/sign_up_page.html', self.params)

    def post(self, request):
        self.user_id = request.POST.get('user_id')
        self.mail = request.POST.get('mail')
        self.pswd = request.POST.get('pswd')
        self.retype_pswd = request.POST.get('re_pswd')
        self.params['msg'] = ""

        #条件に合致しているかの判別プログラム
        dif_pass = (self.pswd != self.retype_pswd)
        already_recorded_mail = self.isin_mail(self.mail)
        already_recorded_id = self.isin_id(self.user_id)
        too_short_pass = self.inough_lengs(self.pswd)
        not_use_id = self.unavailable_cha_id(self.user_id)
        not_use_id = self.available_cha_id(self.user_id)
        not_use_mail = self.unavailable_cha_mail(self.mail)
        not_use_pass = self.unavailable_cha_pass(self.pswd)
        at_isin = self.need_chr_mail(self.mail)
        

        if dif_pass or already_recorded_mail or already_recorded_id or too_short_pass or not_use_id or not_use_mail or not_use_pass or at_isin:
            return_post = request.POST.copy()
            if dif_pass:
                self.params['msg'] += "<br>入力された二つのパスワードが異なります"
            
            if already_recorded_mail :
                self.params['msg'] += "<br>すでに登録してあるメールアドレスです"
            
            if already_recorded_id:
                self.params['msg'] += "<br>すでに登録してあるユーザーIDです"

            if too_short_pass:
                self.params['msg'] += "<br>6文字以上のパスワードを使用してください"
            
            if not_use_id:
                self.params['msg'] += "<br>ユーザーIDに使用できない文字が含まれています"

            if not_use_mail:
                self.params['msg'] += "<br>メールアドレスに使用できない文字が含まれています"

            if not_use_pass:
                self.params['msg'] += "<br>パスワードに使用できない文字が含まれています"
            
            if at_isin:
                self.params['msg'] += "<br>正しいメールアドレスを入力してください"
            
            #formに入力してあったデータを再代入
            self.params['form'] = SignupForm(request.POST)
            return render(request, 'sign_up/sign_up_page.html', self.params)

        else:
            user = User.objects.create_user(self.user_id, self.mail, self.pswd)
            users = UserList(user_id=self.user_id, mail=self.mail)
            users.save()
            user.save()
            return render(request, 'sign_up/sign_up_completed.html')

#sign upが成功した時にサインアップ成功のページに飛ぶ
def comp(request):
    return render(request, "sign_up/sign_up_completed.html")

