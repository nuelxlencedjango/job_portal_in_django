from django.shortcuts import render,redirect

from django.contrib import messages
from .models import Resume
from .forms import *
from account.models import User
# Create your views here.


def updateResume(request):
        if Resume.objects.get(user=request.user).exists():
            resume = Resume.objects.get(user=request.user)
            if request.method == "POST": 
                form = ResumeForm(request.POST,request.FILES, instance=resume)
                if form.is_valid():
                    detail =form.save(commit=False)
                    worker = User.objects.get(id=request.user.id)
                    worker.has_resume =True
                    detail.save()
                    worker.save()
                    messages.warning(request,'Your resume has been updated')
                    return redirect('dashboard:dashboards')

                else:
                    messages.warning(request,'invalid form.Please check your details')  

            form = ResumeForm(instance=resume)
            context={'form':form}
            return render(request,'accounts/update_employer.html',context)   

        return redirect('account:artisan-register') 





def resumeDetails(request,pk):
    if Resume.objects.get(pk=pk).exists():
        resume =Resume.objects.get(pk=pk)
        context ={'resume':resume}
        return render(request,'employees/resume_details.html',context)
    
    return redirect('account:artisan-register') 
         



