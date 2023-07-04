from django.shortcuts import render,redirect

from django.contrib import messages
from .models import Resume
from .forms import *
from account.models import User
# Create your views here.


def updateResume(request):

        #if Resume.objects.filter(user=request.user).exists():
    if request.user.is_applicant and request.method == "POST":     
    #if request.user.is_applicant:
        if Resume.objects.filter(user=request.user).exists():
            resume = Resume.objects.get(user=request.user)
            
            form = ResumeForm(request.POST,request.FILES, instance=resume)
            
            if form.is_valid():
                detail =form.save(commit=False)
                worker = User.objects.get(id=request.user.id)
                    #worker.is_resume =True
                detail.save()
                worker.save()
                messages.warning(request,'Your resume has been updated')
                return redirect('dashboard:dashboards')

            else:
                messages.warning(request,'invalid form.Please check your details')  

                form = ResumeForm(request.POST,instance=resume)
                context={'form':form}
                return render(request,'accounts/update_employer.html',context)   
        

        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
                detail =form.save(commit=False)
                worker = User.objects.get(email=request.user.email)
                worker.is_resume =True
                detail.user = request.user
                worker.save()
                detail.save()
                
                messages.warning(request,'Your resume has been updated')
                return redirect('dashboard:dashboards')
        
    form = ResumeForm()
    context={'form':form}
    return render(request,'accounts/resumee.html',context) 
    
    




def resumeDetails(request,pk):
    if Resume.objects.get(pk=pk).exists():
        resume =Resume.objects.get(pk=pk)
        context ={'resume':resume}
        return render(request,'employees/resume_details.html',context)
    
    return redirect('account:artisan-register') 
         



