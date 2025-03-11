from django.shortcuts import render

def grid_view(request):
    people = [
        {"name": "Meenakshi", "age": 20, "city": "Ongole"},
        {"name": "Dev", "age": 23, "city": "Bhimavaram"},
        {"name": "Charlie", "age": 19, "city": "Rajmundary"},
        {"name": "Devi", "age": 20, "city": "Guntur"},
        {"name": "Bhavya", "age": 21, "city": "Vijayawada"},
    ]
    return render(request, "grid_app/user_list.html", {"people": people})
def table_view(request):
    people = [
        {"name": "Meenakshi", "age": 20, "city": "Ongole"},
        {"name": "Dev", "age": 23, "city": "Bhimavaram"},
        {"name": "Charlie", "age": 19, "city": "Rajmundary"},
        {"name": "Devi", "age": 20, "city": "Guntur"},
        {"name": "Bhavya", "age": 21, "city": "Vijayawada"},
    ]
    return render(request, "grid_app/table.html", {"people":people})