from django.shortcuts import render,redirect
from .models import employee,employeefile
from django.core.files.storage import FileSystemStorage
import csv,io,os
from django.http import HttpResponse,FileResponse,Http404
from tablib import Dataset
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import zipfile
 
def view(request):
    employees=employee.objects.all()
    return render(request,'view.html',{'employees':employees})
def create(request):
    if request.method == 'POST':
        emp_id = request.POST.get('Empid')
        name = request.POST.get('Name')
        mobile = request.POST.get('Mobile')
        email = request.POST.get('Email')
        role = request.POST.get('Role')

        new_employee = employee(
            Empid=emp_id,
            Name=name,
            Mobile=mobile,
            Email=email,
            Role=role,
        )
        new_employee.save()
        files = request.FILES.getlist('file')
        for file in files:
            file_name, file_extension = os.path.splitext(file.name)
            custom_file_name = f"{new_employee.Empid}-{file_name}{file_extension}"
            fs = FileSystemStorage(location='media')
            saved_file = fs.save(custom_file_name, file)
            employeefile.objects.create(employee=new_employee, file=saved_file)
        return redirect('view') 
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
        file_ids = request.POST.getlist('files')  # File IDs submitted via form
        files = employeefile.objects.filter(employee_id=id)

        response = HttpResponse(content_type="application/zip")
        response['Content-Disposition'] = 'attachment; filename="downloaded_files.zip"'

        with zipfile.ZipFile(response, 'w') as zip_file:
            for file_obj in files:
                file_path = os.path.join(settings.MEDIA_ROOT, file_obj.file.name)
                zip_file.write(file_path, os.path.basename(file_path))
        return response  
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