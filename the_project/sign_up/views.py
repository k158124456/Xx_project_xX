from django.shortcuts import render
from django.views.generic import TemplateView
from sign_up.forms import SignupForm
from .models import UserList
# Create your views here.


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

    def get(self, request):
        return render(request, 'sign_up/sign_up_page.html', self.params)

    def post(self, request):
        self.user_id = request.POST.get('user_id')
        self.mail = request.POST.get('mail')
        self.pswd = request.POST.get('pswd')
        self.retype_pswd = request.POST.get('re_pswd')
        self.params['msg'] = ""


        dif_pass = (self.pswd != self.retype_pswd)
        already_recorded_mail = self.isin_mail(self.mail)
        already_recorded_id = self.isin_id(self.user_id)
        too_short_pass = self.inough_lengs(self.pswd)

        if dif_pass or already_recorded_mail or already_recorded_id or too_short_pass:
            return_post = request.POST.copy()
            if dif_pass:
                self.params['msg'] += "<br>入力された二つのパスワードが異なります　"
            
            if already_recorded_mail :
                self.params['msg'] += "<br>すでに登録してあるメールアドレスです　"
            
            if already_recorded_id:
                self.params['msg'] += "<br>すでに登録してあるユーザーIDです　"

            if too_short_pass:
                self.params['msg'] += "<br>6文字以上のパスワードを使用してください　"
            
            self.params['form'] = SignupForm(request.POST)
            return render(request, 'sign_up/sign_up_page.html', self.params)

        else:
            users = UserList(user_id=self.user_id, mail=self.mail, pswd=self.pswd)
            users.save()
            return render(request, 'toppage/toppage.html')
        
        

