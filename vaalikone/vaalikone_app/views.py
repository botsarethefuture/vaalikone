from django.shortcuts import render

from django.template import Context

from .models import Question

def QuestionForm(request, id):
    context = ({"questions": Question.objects.filter(id=id), "next": int(id)+1, "current": int(id)})
    return render(request, context=context, template_name="kissa.html")

def Sek(request):
    print(request.POST)

    return ""