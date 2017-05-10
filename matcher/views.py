from django.shortcuts import render
from django.views import generic
from .models import QuestionInstance, Answers, TrueMatch, Profile, User, Messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.views.generic.edit import FormView
from .forms import AnswerForm, ProfileForm, UserForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db.models import Q

class ExtraContextMixin(object):

    def get_context_data(self, **kwargs):
        context = super(ExtraContextMixin, self).get_context_data(**kwargs)
        context.update(self.extra())
        return context

    def extra(self):
        return dict()

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
    model = QuestionInstance.objects.all()
    template_name = "questioninstance_list.html"

def QuestionList(request):
    model = QuestionInstance.objects.all()
    return render(
        request,
        'questioninstance_list.html',
        context={'questioninstance_list': model}
    )

class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
    model = QuestionInstance
    template_name = "questioninstance_detail.html"

class UserDetailView(LoginRequiredMixin, ExtraContextMixin, generic.DetailView):
    model = User
    template_name = "profiles/view_profile.html"

    def extra(self):
        extra = Profile.objects.all()
        return dict(extra = extra)

class TrueMatchListView(LoginRequiredMixin, generic.ListView):
    model = TrueMatch
    template_name = 'truematch_list.html'
    paginate_by = 10

    def get_queryset(self):
        return TrueMatch.objects.filter(Q(user_onet=self.request.user.id) |
                                      Q(user_twot=self.request.user.id))

class UserAnswersListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listbookinstance_listing books on loan to current user.
    """
    model = Answers
    template_name = 'useranswer_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Answers.objects.filter(user=self.request.user.id)

def answer_question(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form.user = request.user
        print("User: {}".format(request.user))
        if form.is_valid():
            print("Success: {}".format(form))
            form.save()
    else:
        form = AnswerForm()
    return render(request, 'answers_form.html', {'form': AnswerForm()})

class AnswerInstanceView(CreateView):
    template_name = 'answers_form.html'
    #form_class = AnswerForm
    success_url = reverse_lazy('myanswers')

    model = Answers
    fields = ['question', 'answer_option', 'answer_ideal', 'answer_weight']

    def get_initial(self):
        super(AnswerInstanceView, self).get_initial()
        question = QuestionInstance.get_random_question(QuestionInstance)
        self.initial = {"question": question}
        return self.initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.save()
        #success_url = reverse_lazy('myanswers')
        return super(AnswerInstanceView, self).form_valid(form)

class QuestionInstanceView(CreateView):
    model = QuestionInstance
    fields = ['question_text', 'question_option_1', 'question_option_2']
    success_url = reverse_lazy('questions')

    def form_valid(self, form):
        form.instance.submitted_user = self.request.user
        return super(QuestionInstanceView, self).form_valid(form)

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('myprofile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class RegisterView(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('index')

def register_profile(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def view_my_profile(request):
    return render(request, 'profiles/myprofile.html', {
        'user': request.user,
        'profile:': request.user.profile
    })

def get_answer(request):
    if request.method == 'POST':
        form = AnswerForm

        if form.is_valiid():
            print("Success")