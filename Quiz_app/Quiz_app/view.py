from django.shortcuts import redirect, render
import requests


def load_login(request):
    return render(request, 'login.html')

def load_Signup(request):
    return render(request, 'signup.html')

def index(request):
    return render(request, 'index.html')

def load_page(request):
    if request.POST.get('submit') == 'Log out':
        return redirect('load_login')
    elif request.POST.get('submit') == 'start':
        return redirect('load_Signup')
    else:    
        return redirect('index')
        
def save_details(request):
    print(request.POST.get('name'))
    print(request.POST.get('passw'))
    user_details =  requests.post("http://127.0.0.1:8000/user_login",data={"name":request.POST.get('name'),"passw":request.POST.get('passw')}) 
    print(user_details.json())
    return render(request, 'index.html')

def check_details(request):
    user_details = requests.get("http://127.0.0.1:8000/user_login",data={"name":request.POST.get('name'),"passw":request.POST.get('passw')})
    print(user_details.json())
    return redirect('index')