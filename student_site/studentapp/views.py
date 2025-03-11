from django.shortcuts import render

# Create your views here.
def std_list(request):
    students = [
        {'name': 'Aparna', 'marks': 55},
        {'name': 'pavani', 'marks': 69},
        {'name': 'Sai', 'marks': 90},
        {'name': 'Mythri', 'marks': 39},
    ]
    passing_marks = 40 # Define passing marks threshold
    return render(request, 'student_app/std_list.html', {'students': students, 'passing_marks': passing_marks})
