from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import NewsSources, NewsContents, AuthUser
from .forms import AddSource_Form, UpdateSource_Form, AddNews_Form, UpdateNews_Form, AddUser_form, UpdateUser_form



class NewsSources_ListView(ListView):
    context_object_name = 'sources'
    model = NewsSources
    template_name = 'news/sources_list.html'



class NewsSources_CreateView(CreateView):
    model = NewsSources
    form_class = AddSource_Form
    success_url = reverse_lazy("news_sources")
    template_name = 'news/source_add.html'



class NewsSources_DeleteView(DeleteView):
    model = NewsSources
    context_object_name = 'source'
    success_url = reverse_lazy('news_sources')
    template_name = 'news/source_delete.html'



class NewsSources_UpdateView(UpdateView):
    model = NewsSources
    form_class = UpdateSource_Form
    success_url = reverse_lazy('news_sources')
    template_name = 'news/source_update.html'



class NewsContents_ListView(ListView):
    context_object_name = 'contents'
    model = NewsContents
    page_kwarg = 'page'
    paginate_by = 5
    template_name = 'news/contents_list.html'
    ordering = ['-news_date_time']



class NewsContents_CreateView(CreateView):
    model = NewsContents
    form_class = AddNews_Form
    success_url = reverse_lazy('news_contents')
    template_name = 'news/content_add.html'



class NewsContents_DeleteView(DeleteView):
    model = NewsContents
    ordering = ['-news_date_time']
    context_object_name = 'content'
    success_url = reverse_lazy('news_contents')
    template_name = 'news/content_delete.html'



class NewsContents_UpdateView(UpdateView):
    model = NewsContents
    form_class = UpdateNews_Form
    context_object_name = 'content'
    success_url = reverse_lazy('news_contents')
    template_name = 'news/content_update.html'



class AuthUser_ListView(ListView):
    context_object_name = 'users'
    model = AuthUser
    page_kwarg = 'page'
    paginate_by = 10
    template_name = 'news/users_list.html'



class AuthUser_CreateView(CreateView):
    model = AuthUser
    form_class = AddUser_form
    success_url = reverse_lazy('users')
    template_name = 'news/user_add.html'



class AuthUser_UpdateView(UpdateView):
    model = AuthUser
    form_class = UpdateUser_form
    context_object_name = 'content'
    success_url = reverse_lazy('users')
    template_name = 'news/user_update.html'
