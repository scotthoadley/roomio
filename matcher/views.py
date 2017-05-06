from django.shortcuts import render
from django.views import generic
from .models import QuestionInstance, Answers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.views.generic.edit import FormView
from .forms import AnswerForm, ProfileForm, UserForm
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_questions = QuestionInstance.objects.all().count()
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_questions': num_questions},
    )

class QuestionListView(LoginRequiredMixin, generic.ListView):
    model = QuestionInstance
    template_name = "questioninstance_list.html"

class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
    model = QuestionInstance
    template_name = "questioninstance_detail.html"

class UserAnswersListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listbookinstance_listing books on loan to current user.
    """
    model = Answers
    template_name = 'useranswer_list.html'
    paginate_by = 10

    #def get_queryset(self):
        #return Answers.objects.filter(created_by=self.request.user_id)

class AnswerView(generic.FormView):
    template_name = 'answers_form.html'
    form_class = AnswerForm
    success_url = reverse_lazy('myanswers')

    def form_valid(self, form):
        #form.instance.created_by = self.request.user
        form.save(commit=False)
        return super(AnswerView, self).form_valid(form)

# class AnswerView(CreateView):
#     model = Answers
#     fields = ['question', 'answer_option', 'answer_weight']
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super(AnswerView, self).form_valid(form)
#         #success_url = reverse_lazy('my-answers')

class QuestionInstanceView(CreateView):
    model = QuestionInstance
    fields = ['question_text', 'question_option_1', 'question_option_2', 'question_option_3', 'question_option_4']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(QuestionInstanceView, self).form_valid(form)
        #success_url = reverse_lazy('my-answers')

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })