from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app2.forms import BmiForm #参照元からの相対パスを書く必要がある

class BmiView(TemplateView):
    def __init__(self):
        self.parms = {
            "title" : "Hello",
            "msg"  : "your data",
            "form" : BmiForm(),
        }

    def get(self, request):
        return render(request, "app2/form.html", self.parms)
    
    def post(self, request):
        weight = request.POST["weight"]
        hight = request.POST["hight"]
        BMI = float(weight) * (float(hight)/100)**2

        self.parms["msg"] = "身長:" + hight + "<br>体重:" + weight + "<br>BMIは:"+str(BMI)[:5]+"です"
        self.parms["form"] = BmiForm(request.POST) #ここでpostされている内容を再代入する。

        return render(request, "app2/form.html", self.parms)

def index(request):
    return 0
    
    
    