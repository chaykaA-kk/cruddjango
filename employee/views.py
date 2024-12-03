from django.shortcuts import render ,redirect 
from employee.models import Employee
from employee.forms import EmployeeForms

def emp(request):
    
    if request.method== "POST": 
        form=EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form=EmployeeForms()
    return render(request,'index.html',{'form':form})    
def show (request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employee':employees})


def edit (request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})
    #employees=employe


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForms(request.POST , instance=employee)  
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})



def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
