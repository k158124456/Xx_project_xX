from django.shortcuts import render

# Create your views here.

def app_1_index(request):
    dict_1={
        'str_1':'app_1_indexのdict_1のstr_1を表示してる',
        'name':'yarita'
    }
    return render(request,'app_1/app_1_index.html',dict_1)