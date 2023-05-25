from django.shortcuts import render,redirect 
from django.contrib import  messages
from django.utils import timezone
from resume.models import *
from .models import *
from .forms import *




def create_job(request):
    if request.user.is_recruiter and request.user.has_company:

        if request.method == 'POST':
            form = CreateJobForm(request.POST) 
            if form.is_valid():
                job = form.save(commit=False)
                job.user =request.user
                job.employers =request.user.user
                job.save()
                messages.success(request, 'Job created successfully. ' )
                return redirect('dashboard:dashboards')

            else:
                messages.info(request, 'Job not created.Something went wrong ' )
                return redirect('job:create-job')
        
        else:
            form = CreateJobForm()
            context = {'form':form}   
            return render(request, 'jobs/create_jobs.html', context)
        

    messages.success(request, 'Access Denied ' )
    return redirect('dashboard:dashboards')   





def updateJob(request,pk):
    job = JobsCreated.objects.get(pk=pk)
    if request.method == 'POST':
        form = JobUpdateForm(request.POST,instance=job) 
        if form.is_valid():
            job.save()
            messages.success(request, 'Job details updated successfully. ' )
            return redirect('dashboard:dashboards')

        else:
            messages.info(request, 'Job not updated.Something went wrong ' )
            #return redirect('')
    
    else:
        form = JobUpdateForm(instance=job)
        context = {'form':form}   
        return render(request, 'jobs/update_job_info.html', context)
    


def applied_jobs(request):
    appliedJobs=ApplyJob.objects.filter(user =request.user)
    context={'appliedJobs':appliedJobs}
    return render(request, 'jobs/appliedJobs.html', context)

