from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from.models import post,category,comment
from.forms import postform
from.forms import Edit,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(ListView):
    model = post
    template_name = 'home.html'
    paginate_by = 10
    ordering = ['-postdate']

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-postdate')
        return queryset
# Create your views here.
class articledetail(DetailView):
    model=post
    template_name = 'articledetail.html'
class Addpost(LoginRequiredMixin,CreateView):
    model=post
    form_class = postform
    template_name = 'post.html'

    def form_valid(self,form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

class category(CreateView):
    model=category
    fields = '__all__'
    template_name = 'category.html'
class update(UpdateView):
    model=post
    form_class = Edit
    template_name = 'update.html'
    #fields = ['title','title_tag','body']
class delete(DeleteView):
    model=post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model= comment
    form_class = CommentForm
    template_name = 'add_comments.html'    
    success_url = reverse_lazy('home')
    # fields = '__all__'

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)