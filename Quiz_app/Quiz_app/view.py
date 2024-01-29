from django.shortcuts import redirect, render
from pprint import pprint
import requests



def load_login(request,info=""):
    print(info)
    return render(request, 'login.html', {'info':info})

def load_Signup(request):
    return render(request, 'signup.html')

def index(request):
    return render(request, 'index.html')

def load_page(request):
    if request.POST.get('submit') == 'Log out':
        return redirect('load_login')
    elif request.POST.get('submit') == 'start':
        user_details =  requests.get("http://127.0.0.1:8000/mcq_data")
        pprint(user_details.json())
        return render(request,'load_mcqs.html',{'all_mcq':user_details.json(),'count':0})
    else:    
        return redirect('index')
        
def save_details(request):
    print(request.POST.get('name'))
    print(request.POST.get('passw'))
    user_details =  requests.post("http://127.0.0.1:8000/user_login",data={"name":request.POST.get('name'),"passw":request.POST.get('passw')}) 
    print(user_details.json())
    return render(request, 'index.html')

def check_details(request):
    user_details = requests.get("http://127.0.0.1:8000/user_login",data={"name":request.POST.get('name'),"passw":request.POST.get('passw')}).json()
    if user_details['status_code'] == 200:
        request.session['user_name'] = user_details['Data']['name']
        print(request.session.get('user_name'))
        return redirect('index')
    return render(request, 'login.html',{'info':"Invalid details please try again"})