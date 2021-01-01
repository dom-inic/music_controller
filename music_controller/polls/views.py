from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.http import JsonResponse



from .models import Question, Choice

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ',' .join([q.question_text for q in latest_question_list])
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)

# 	try:
# 		selected_choice = question.choice_set.get(pk=request.POST['choice'])
# 	except (KeyError, Choice.DoesNotExist):

# 		""" redisplay the question voting form"""
# 		context= {'question': question, 'error_message': "you didn't select a choice"}
# 		return render(request, 'polls/detail.html', context )

# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 		# always return an httpresponseredirect after successfully dealing
# 		# with post data. this prevents data from being posted twice if a 
# 		# user hits the back buton
# 		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    

# class IndexView(generic.ListView):
# 	template_name = 'polls/index.html'
# 	context_object_name = 'latest_question_list'

# 	def get_queryset(self):
# 		""" return the last five published questions """
# 		return Question.objects.order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
# 	model = Question
# 	template_name = 'polls/detail.html'

# class ResultsView(generic.DetailView):
# 	model = Question
# 	template_name = 'polls/results.html'

def polls_list(request):
	MAX_OBJECTS = 20
	polls = Question.objects.all() [:MAX_OBJECTS]
	data = {"results": list(polls.values("question_text", "created_by__username", "pub_date"))}
	return JsonResponse(data)

def polls_detail(request, pk):
	poll = get_object_or_404(Question, pk=pk)
	data = {"results": {
		"question":poll.question,
		"created_by": poll.created_by.username,
		"pub_date" : poll.pub_date
	}}
	return JsonResponse(data)