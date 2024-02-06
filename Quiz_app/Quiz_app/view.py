from django.shortcuts import redirect, render
from pprint import pprint
import requests
global mcqs_questions, user_info

def load_login(request,info=""):
    return render(request, 'login.html', {'info':info})

def load_Signup(request):
    return render(request, 'signup.html')

def index(request):
    return render(request, 'index.html')

def load_page(request):
    global mcqs_questions
    if request.POST.get('submit') == 'Log out':
        return redirect('load_login')
    elif request.POST.get('submit') == 'start':
        mcqs_questions =  requests.get("http://127.0.0.1:8000/mcq_data").json()
        return render(request,'load_mcqs.html',{'all_mcq':mcqs_questions,'count':0})
    else:
        del request.session['user_name']
        return redirect('index')
        
def save_details(request):
    requests.post("http://127.0.0.1:8000/user_login",data={"name":request.POST.get('name'),"passw":request.POST.get('passw')})
    return render(request, 'login.html')

def check_details(request):
    global user_info
    user_details = requests.get("http://127.0.0.1:8000/user_login",data={"name":request.POST.get('name'),"passw":request.POST.get('passw')}).json()
    print(user_details)
    if user_details['status_code'] == 200:
        request.session['user_name'] = user_details['Data']['name']
        user_info = {'id':user_details['Data']['id'],'name':user_details['Data']['name']}
        return redirect('index')
    return render(request, 'login.html',{'info':"Invalid details please try again"})

def user_answer(request):
    global mcqs_questions,user_info
    pprint(mcqs_questions)
    all_answers = []
    for x in range(1,4):
        all_answers.append({'number':x,'user_input':request.POST.get(str(x)),"answer":mcqs_questions[x-1]['answer']})
    mcqs_questions = 0
    for x in all_answers:
        if x['user_input'] == x['answer'] :
            mcqs_questions += 1
    print(requests.post("http://127.0.0.1:8000/mcq_data",data={'id':user_info['id'],'name':user_info['name'],'total_score':mcqs_questions}))
    
    return redirect('index')

