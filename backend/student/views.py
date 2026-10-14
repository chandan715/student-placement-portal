from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse 

@api_view(['GET'])
def student_list(request):
    students = [
        {"id": 1, "name": "Rahul", "course": "Python"},
        {"id": 2, "name": "Priya", "course": "Full Stack Development"},
    ]
    return Response({"students": students})