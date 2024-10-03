from django.shortcuts import render,redirect
from .models import employee
from django.core.files.storage import FileSystemStorage
import csv,io,os
from django.http import HttpResponse,FileResponse,Http404
from tablib import Dataset
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

def view(request):
    employees=employee.objects.all()
    return render(request,'view.html',{'employees':employees})
def create(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            emp_id = request.POST.get('Empid')
            name = request.POST.get('Name')
            mobile = request.POST.get('Mobile')
            email = request.POST.get('Email')
            role = request.POST.get('Role')
            files = request.FILES.getlist('file')
            file_paths = []
            uploaded_files_urls=[]
            fs = FileSystemStorage(location='media')
            for file in files:
                filename = fs.save(str(emp_id)+"-"+file.name, file)
                uploaded_file_url = fs.url(filename)
                uploaded_files_urls.append(uploaded_file_url)
                file_paths.append(filename)
            new_employee = employee(
                Empid=emp_id,
                Name=name,
                Mobile=mobile,
                Email=email,
                Role=role,
                file=filename
            )
            new_employee.save()
            return redirect('view') 
        else:
            return render(request, 'view.html')
    return render(request, 'view.html')
def update(request):
    if request.method =='POST':
        id = request.POST.get('update-id')
        empid = request.POST.get('Empid')
        name = request.POST.get('Name')
        mobile = request.POST.get('Mobile')
        email = request.POST.get('Email')
        role = request.POST.get('Role')
        update_filter = employee.objects.filter(id=id).update(
            Empid = empid, Name = name, Mobile = mobile, Email = email, Role = role)
        return redirect('view')
    return redirect('update')
def delete(request,id):
    form=employee.objects.get(id=id)
    form.delete()
    return redirect('view')
def download_file(request, id):
    try:
        uploaded_file = employee.objects.get(id=id)
        return FileResponse(uploaded_file.file, as_attachment=True)
    except employee.DoesNotExist:
        raise Http404("File not found")
def importfile(request):
    if request.method == 'POST':
        file = request.FILES['csv_file']
        data = pd.read_excel(file)
        data.fillna('', inplace=True)
        for index, row in data.iterrows():
            employee(
            Empid= row['Empid'],
            Name = row['Name'],
            Mobile = row['Mobile'],
            Email = row['Email'],
            Role = row['Role']
            ).save()
        return redirect('view')
    return render(request, 'importfile.html')