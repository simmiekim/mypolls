from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

"""
def index(request):
    # return HttpResponse("안녕 장고")
    contents = '''
        <html>
            <body>
                <h1>나의 장고</h1>
                <p>우리는 할 수 있다</p>
            </body>
        </html>
    '''
    return HttpResponse(contents)
"""
"""
    메소드 : index
    인자 : request
    리턴 : HttpResponse
"""

from polls.models import Question, Choice
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    latest_question_list = Question.objects.all()
    # print(latest_question_list)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# 로깅 추가
# import logging
# logger = logging.getLogger(__name__)
# logger = logging.getLogger('polls')

def vote(request, question_id):
    # 로깅 추가
    # logger.debug("vote().question_id: %s" % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # 경로 :  /polls/3/results/
        # 에러남 : return HttpResponseRedirect('/polls/'+question_id+'/results/')
        # next = '/polls/'+str(3)+'/results/'
        # print(next)
        # return HttpResponseRedirect('/polls/'+str(question_id)+'/results/')

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
