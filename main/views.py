from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    DetailView,
    ListView,
    FormView
)

from django.views.generic.detail import SingleObjectMixin

from main import models,forms

class Index(ListView):
    model = models.Question
    template_name = 'main/index.html'
    context_object_name = 'questions_list'

class Question(SingleObjectMixin,FormView):
    model = models.Question
    template_name = 'main/question.html'
    form_class = forms.AnswerForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        count = models.Answer.objects.filter(user = self.request.user).count()
        question_count = models.Question.objects.all().count()
        if(count==question_count):
            data['answer'] = models.Answer.objects.get(question = self.get_object(),user = self.request.user)
        else:
            data['answer'] = None
        print(data['answer'])
        return data
    
    def form_valid(self,form):
        print("running")
        obj = form.save(commit = False)
        obj.user = self.request.user
        obj.question = self.get_object()
        obj.save()
        return HttpResponse('/')
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request,*args,**kwargs)