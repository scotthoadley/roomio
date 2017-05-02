from django.shortcuts import render
from django.views import generic
from .models import QuestionInstance


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
class QuestionListView(generic.ListView):
    model = QuestionInstance
    template_name = "questioninstance_list.html"

class QuestionDetailView(generic.DetailView):
    model = QuestionInstance
    template_name = "questioninstance_detail.html"