from django.shortcuts import render,redirect  #,get_object_or_404
from django.contrib import auth, messages
from django.utils import timezone
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
#from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q 
#from django.core.mail import send_mail

from account.models import *    
from employers.models import *   
from resume.models import *        
from .models import *
from .forms import *







#artisans registration

def artisans_registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
         
        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_applicant =True
            profile.username =profile.email
            profile.save()

            Resume.objects.create(user=profile)
            messages.success(request, 'Account successfully created. Please login ' )
            return redirect('account:login')

        else:
            messages.info(request, 'Something went wrong ' )
            return redirect('account:artisan-register')
    
    else:
        form = SignUpForm()
        context = {'form':form}   
        return render(request, 'accounts/artisan_register.html', context)



#employers registration
def employer_registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
         
        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_recruiter =True
            profile.username =profile.email

            profile.save()
            Employers.objects.create(user=profile)
            messages.success(request, 'Account successfully created. Please login ' )
            return redirect('account:login')

        else:
            messages.info(request, 'Something went wrong ' )
            return redirect('account:employer_register')
    
    else:
        form = SignUpForm()
        context = {'form':form}   
        return render(request, 'accounts/employers_register.html', context)




# client and artisan loggining into account
def loginPage(request):
    if request.method == 'POST':
    
        email = request.POST.get('email')
        password =request.POST.get('password')
        
        #authenticate the user and log the user in if authenticated and exists
        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_active:
            login(request,user)
            return redirect('dashboard:dashboards')

            # if the user is an artisan and already registered,log him in
            #if request.user.is_applicant:  
                #return redirect('account:artisan-dashboard')
            
            # if the user is an employer and already registered,log him in
            #elif request.user.is_recruiter:
             #   return redirect('account:employer-dashboard')
               
           #if user is a superuser
           # elif user.is_superuser:
            #    login(request,user)
             #   return redirect('account:admin_page')
        
            #if none is correct,username or password is incorrect
            #else:
             #   messages.info(request, 'Something went wrong')
              #  return redirect('account:login')

        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('account:login')        

    context = {}
    return render(request, 'accounts/login.html', context)








#logout 
@login_required
def logoutPage(request):
    logout(request)
    return redirect('account:home')