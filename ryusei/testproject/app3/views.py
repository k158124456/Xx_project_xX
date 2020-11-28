from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from app3.forms import IdForm

# Create your views here.
def index(request):

    data = Friend.objects.all()
    params = {
        'title' : 'Hello',
        'message' : 'all friends.',
        'data' : data,
        'form' : IdForm()
    }
    if request.method == 'POST':
        num = request.POST['id']
        if num=="0":
            params['data'] = Friend.objects.all()
            params['message'] = 'all friends'
            
        else:
            params['data'] = [Friend.objects.get(id=num)]
            params['message'] = 'Friend whose id is ' + str(num)
        params['form'] = IdForm(request.POST)
    return render(request, 'app3/toppage.html', params)