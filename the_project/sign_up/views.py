from django.shortcuts import render
from django.views.generic import TemplateView
from sign_up.forms import SignupForm
# Create your views here.


class SignUp(TemplateView):
    def __init__(self):
        self.params = {
            'form' : SignupForm(),
            'msg' : "",
        }
    def get(self, request):
        return render(request, 'sign_up/sign_up_page.html', self.params)

    def post(self, request):
        self.iser_id = request.POST.get('user_id')
        self.mail = request.POST.get('mail')
        self.pswd = request.POST.get('pswd')
        self.retype_pswd = request.POST.get('re_pswd')
        self.params['msg'] = ""

        dif_pass = self.pswd == self.retype_pswd
        aleady_recorded = False
        too_short_pass = False

        if dif_pass or aleady_recorded or too_short_pass:
            return_post = request.POST.copy()
            return_post['re_pswd'] = ''
            return_post['pswd'] = ''
            if dif_pass:
                self.params['msg'] += "入力された二つのパスワードが異なります　"
            
            if aleady_recorded :
                self.params['msg'] += "すでに登録してあるIDです　"
            
            if too_short_pass:
                self.params['msg'] += "五文字以上のパスワードを使用してください　"
            
            self.params['form'] = SignupForm(return_post)
            return render(request, 'sign_up/sign_up_page.html', self.params)
        

        else:
            return render(request, 'sign_up/sign_up_page.html', self.params)
        

