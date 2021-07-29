from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from imageDuplicates.models import Question

from .models import Question
# Create your views here.
class IndexView(generic.ListView):
    template_name='imageDuplicates/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """return the last five published questions."""
        return Question.objects.order_by()[:]

class DetailView(generic.DetailView):
    model=Question
    template_name='imageDuplicates/detail.html'

class ResultsView(generic.DetailView):
    model=Question
    template_name='imageDuplicates/results.html'    

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form.
        return render(request,'imageDuplicates/detail.html',{
            'question' : question,
            'error_message' : "you didn't select a choice."
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('imageDuplicates:results',args=(question.id,)))

def search(request):
    query = request.GET['query']
    allQuestion = Question.objects.filter(question_text__icontains=query)
    params = {'allQuestion':allQuestion}
    return render(request,"imageDuplicates/search.html",params)
    # return HttpResponse("this is my search page")