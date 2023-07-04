from django.shortcuts import render,redirect 
from django.contrib import  messages
from job.models import *
from .filters import JobFilter
# Create your views here.


def index(request):
    filter = JobFilter(request.GET, queryset=AvailableJobs.objects.filter(is_available=True).order_by('-date_created'))
    context={'filter':filter}
    return render(request,'general/index.html',context)



def jobListing(request):
    available_jobs = AvailableJobs.objects.filter(is_available=True).order_by('-timestamp')
    context={'available_jobs':available_jobs}

    return render(request,'jobs/available_jobs.html',context)



def jobDetails(request,pk):
    if  request.user.is_authenticated:

        if ApplyJob.objects.filter(user=request.user,job=pk).exists():
            has_applied = True
        else:
            has_applied = False
            
        job_details = AvailableJobs.objects.get(pk=pk)   
        context={'job_details':job_details,"has_applied":has_applied}
        return render(request,'jobs/job_details.html',context)
        
    else:
        messages.info(request,'You have to login first,please.')   
        return redirect('account:login')  
    
    



def manageJobsCreated(request):
    if AvailableJobs.objects.filter(user=request.user,employers=request.user.employer).exists():
        allJobs =AvailableJobs.objects.filter(user=request.user,employers=request.user.employer)
        context={'allJobs':allJobs}
        return render(request,'jobs/all_employers_posted_jobs.html',context)
    
    messages.info(request,'You have not posted any job yet')
    return render(request,'jobs/all_employers_posted_jobs.html')



def apply_to_job(request,pk):
    if request.user.is_authenticated:
        job =AvailableJobs.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user,job=pk).exists():
            messages.warning(request,"You have already applied for this job")
            return redirect('dashboard:dashboards')
        
        else:
            if request.user.is_resume:
                ApplyJob.objects.create(job=job,user=request.user, status='Pending')
                
                messages.info(request,'You have successfully applied')
                return redirect('dashboard:dashboards')
            
            return redirect('resume:resume_update')
        

    messages.info(request,'You need to login before you can apply for a job.')
    return redirect('account:login')
    

def all_applicants(request,pk):
    job =AvailableJobs.objects.get(pk=pk)
    applicants =job.applyjob_set.all()
    context={'job':job, 'applicants':applicants}
    return render(request,'job/all_applicants.html',context)
