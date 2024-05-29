# myapp/views_html.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import JobSeeker, AdminUser, Job

def home(request):
    return render(request, 'Home.html')

# Job Seeker Views
def jobseeker_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        JobSeeker.objects.create(name=name, mobile=mobile)
        return redirect('jobseeker_list')
    return render(request, 'jobseeker_form.html')

def jobseeker_update(request, id):
    jobseeker = get_object_or_404(JobSeeker, id=id)
    if request.method == 'POST':
        jobseeker.name = request.POST['name']
        jobseeker.mobile = request.POST['mobile']
        jobseeker.save()
        return redirect('jobseeker_list')
    return render(request, 'jobseeker_update_form.html', {'jobseeker': jobseeker})

# def jobseeker_delete(request, id):
#     jobseeker = get_object_or_404(JobSeeker, id=id)
#     if request.method == 'POST':
#         jobseeker.delete()
#         return redirect('jobseeker_list')
#     return render(request, 'jobseeker_confirm_delete.html', {'jobseeker': jobseeker})

def jobseeker_confirm_delete(request, id):
    jobseeker = JobSeeker.objects.get(id=id)
    if request.method == 'POST':
        jobseeker.delete()
        return redirect('jobseeker_list')
    return render(request, 'jobseeker_confirm_delete.html', {'jobseeker': jobseeker})

def jobseeker_list(request):
    jobseekers = JobSeeker.objects.all()
    return render(request, 'jobseeker_list.html', {'jobseekers': jobseekers})

# Admin User Views
def adminuser_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        AdminUser.objects.create(name=name, email=email)
        return redirect('adminuser_list')
    return render(request, 'adminuser_form.html')

def adminuser_update(request, id):
    adminuser = get_object_or_404(AdminUser, id=id)
    if request.method == 'POST':
        adminuser.name = request.POST['name']
        adminuser.email = request.POST['email']
        adminuser.save()
        return redirect('adminuser_list')
    return render(request, 'adminuser_update_form.html', {'adminuser': adminuser})

def adminuser_delete(request, id):
    adminuser = get_object_or_404(AdminUser, id=id)
    if request.method == 'POST':
        adminuser.delete()
        return redirect('adminuser_list')
    return render(request, 'adminuser_confirm_delete.html', {'adminuser': adminuser})

def adminuser_list(request):
    adminusers = AdminUser.objects.all()
    return render(request, 'adminuser_list.html', {'adminusers': adminusers})

# Job Views
def job_create(request):
    if request.method == 'POST':
        job_title = request.POST['job_title']
        job_description = request.POST['job_description']
        Job.objects.create(job_title=job_title, job_description=job_description)
        return redirect('job_list')
    return render(request, 'job_form.html')

def job_update(request, id):
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        job.job_title = request.POST['job_title']
        job.job_description = request.POST['job_description']
        job.save()
        return redirect('job_list')
    return render(request, 'job_update_form.html', {'job': job})

def job_delete(request, id):
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'job_confirm_delete.html', {'job': job})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})
