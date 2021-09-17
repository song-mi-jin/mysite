#from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from polls.models import Choice, Question

class PollsListView(ListView):
    model = Question
##def index(request):
##    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
##    context = {'latest_question_list': latest_question_list}
##    #print(context)
##    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    print(KeyError)
    #print(question.choice_set.all())
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    
    #question = get_object_or_404(Question, pk=question_id)
    #selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice = Choice.objects.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    ## update from Choice set votes=votes+1 where id=request.POST['choice']
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    
