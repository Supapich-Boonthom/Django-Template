import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def home(request):
    context = {
        "title": "My Home Page",
    }

    students = Student.objects.all()

    context["students"] = students

    context["date"] = datetime.date.today()
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)

    context = {"student": student}

    return render(request, "student_detail.html", context)
