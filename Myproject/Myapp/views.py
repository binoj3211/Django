from django.shortcuts import render

from django.http import HttpResponse
from Myapp.models import Question,Choice

# Create your views here.


def index(request):
    return HttpResponse('Hello')

def question_1(request):
    questions = Question.objects.all()
    return render(request,'question_list.html',{'questions':questions})
    # All_question=Question.objects.all()
    # return HttpResponse(All_question)


# def question_list(request):

#     context ={}

#     context["dataset"] = Question.objects.all()

#     return render(request,"ques.html",context)




def choice_list(request,id):

    context ={}

    context["dataset"] = Choice.objects.filter(question=id)

    return render(request,"choice_list.html",context)
