from django.shortcuts import render
from django.views import generic
from .models import QuestionInstance, Answers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


# class BookListView(generic.ListView):
#     model = Book
#     context_object_name = 'my_book_list'   # your own name for the list as a template variable
#     queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
#     template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/locati
#
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

class AnswersCreate(CreateView):
    model = Answers
    fields = ['question', 'answer_option', 'answer_weight']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(AnswersCreate, self).form_valid(form)
        #success_url = reverse_lazy('my-answers')