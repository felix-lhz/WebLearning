from django.shortcuts import render,HttpResponse,redirect
import requests

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django!")

def userList(request):
    return HttpResponse("User List")

def userAdd(request):
    return HttpResponse("User Add")

def news(request):
    res = requests.get("http://news.baidu.com/")
    data_list = res.content.decode("utf-8")
    # print(data_list)
    return render(request, "news.html", {"data_list": data_list})

def login(request):
    if request.method=="POST":
        return render(request, "login.html")
    
    #如果是POST请求，获取用户提交的数据
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == "root" and password == "123":
        return redirect("http://www.baidu.com")
    
    return render(request, "login.html", {"error": "用户名或密码错误"})