from django.shortcuts import render,redirect

# Create your views here.

'''
def proxy(request):
    if request.user.is_applicant:
        return redirect('dashboard:artisan-dashboard')
    elif user.is_recruiter :
        return redirect('dashboard:employer-dashboard') 
    else:
        return redirect('account:login')       


def artisanDashboard(request):
    context={}
    return render(request,'dashboard/artisans_dashboard.html',context)



def employerDashboard(request):
    context={}
    return render(request,'dashboard/employers_dashboard.html',context)
'''

def users_dashboard(request):
    context={}
    return render(request,'dashboard/dashboard.html',context)

