from django.shortcuts import render
from django.shortcuts import redirect 
from .forms import StudentForm
from .models import Student

# Create your views here.
def studentview(request):
    if request.method =='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=StudentForm()
    return render(request,'student.html',{'form':form})

def student_list(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})
