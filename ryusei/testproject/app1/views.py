from django.shortcuts import render

import random
# Create your views here.
def index(request):
    title = "Hello. This is Top Page."
    page1 = "app1_page1"
    page2 = "app1_page2"
    params = {
        "title": title,
        "page1":page1,
        "page2":page2,

    }
    return render(request, "app1/toppage.html",params)

def page1(request):
    title = "app1_page1"
    toppage = "app1:toppage"
    params = {
        "title": title,
        "back": toppage,
    }
    return render(request, "app1/page.html",params)

def page2(request):
    title = "app1_page2"
    toppage = "app1:toppage"
    contains = ["aaa" for a in range(100)]
    params = {
        "title": title,
        "back": toppage,
        "contains": contains
    }
    return render(request, "app1/page.html",params)