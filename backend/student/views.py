from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to Student Placement Portal")


def student_list(request):
    students = [
        {"id": 1, "name": "Rahul", "course": "Python"},
        {"id": 2, "name": "Priya", "course": "Full Stack Development"},
    ]

    return JsonResponse({"students": students})
 





