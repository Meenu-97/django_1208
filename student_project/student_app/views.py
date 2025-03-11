from django.shortcuts import render, HttpResponse
from .models import Student

def add_student(request):
    student = Student(name="Meenakshi", age=19, email="meenakshi@gmail.com")
    student.save()
    return HttpResponse("Student record added successfully!")
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})