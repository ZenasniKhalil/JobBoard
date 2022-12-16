from django.shortcuts import render
from .models import JobModel, Requirements
# Create your views here.

def home(request):
    context = {
        
    }
    return render(request, 'job/home.html', context)

def job_detail(request, pk):
    job = JobModel.objects.get(pk=pk)
    requirements = Requirements.objects.filter(job_title=job)
    context = {
        'job':job,
        'requirements':requirements,
    }
    return render(request, 'job/job_detail.html', context)

def job_listing(request):
    jobs = JobModel.objects.all()
    context = {
        'jobs':jobs,
    }
    return render(request, 'job/job_listing.html', context)
