from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
from account.models import User



def updateCompany(request):
    
    if Employers.objects.get(user=request.user).exists():

        company = Employers.objects.get(user=request.user)
        if request.method == "POST":
            form = UpdateCompanyForm(request.POST, instance=company)
            if form.is_valid():
                comp =form.save(commit=False)
                employer = User.objects.get(id=request.user.id)
                employer.has_company =True
                comp.save()
                employer.save()

                messages.warning(request,'Your details have been updated')

            else:
                messages.warning(request,'invalid form.Please check your details')  

        
        form = UpdateCompanyForm(instance=company)
        context={'form':form}
        return render(request,'accounts/update_employer.html',context)   

    return redirect('account:employer_register') 



def emploerDetails(request,pk):
    company =Employers.objects.get(pk=pk)
    if company:
        context={'company':company}
        return render(request,'aacounts/employer_details.html')
    
    messages.info(request,'Information not found')
    return render(request,'aacounts/employer_details.html')