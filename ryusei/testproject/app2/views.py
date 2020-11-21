from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app2/form.html")

def form(request):
    hight = request.POST["hight"]
    weight = request.POST["weight"]
    BMI = float(weight) / (float(hight)/100)**2
    parms = {
        "msg"  : "あなたのBMIは" + str(BMI)[:6]+ "です"
    }
    return render(request, "app2/form.html", parms)
    