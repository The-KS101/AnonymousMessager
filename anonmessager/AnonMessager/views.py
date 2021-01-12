from django.shortcuts import render, redirect, get_object_or_404
from .models import Message, User
from django.http import HttpResponseRedirect
from .forms import MessagingForms, ProfileForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.

def sendMessage(request, username):
    username = username
    userMes = User.objects.get(username=username)
    if request.method == "POST":
        form = MessagingForms(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.userMessage = userMes
            model_instance.save()
            return redirect('AnonMessager:joinen')
    else:    
        form = MessagingForms()
    content = {
        'form': form,
        'username': username
    }
    return  render(request, 'anonMessager/index.html', content)


    

def join(request):
    success = "Message sent"
    if request.method == "POST":
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            
            context =  {
                'username': user.username,
                
            }

            return render(request,'anonMessager/success.html', context)

            
    else:
        form = ProfileForm()
    content = {
            "form": form,
            'success': success,
        }
    return render(request, 'anonMessager/createYourAccount.html', content)


def messages(request, username):
    user = get_object_or_404(User, username=username)

    message = Message.objects.filter(userMessage = user)
    messager = message.order_by('-pub_date')

    
    context={"message": messager}

    return render(request, 'anonMessager/messages.html', context)

def loginFunction(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)        
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('AnonMessager:message', username)

    else:
        form = LoginForm()
    content = {
                'form':form
            }
    return render(request, 'anonMessager/login.html', content)
