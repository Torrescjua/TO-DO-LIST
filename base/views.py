from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    """
    View to handle user login.
    """
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterUser(FormView):
    """
    View to handle user registration.
    """
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        """
        If the form is valid, save the new user and log them in.
        """
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def get(self, *args, **kwargs):
        """
        If user is authenticated, redirect to tasks.
        """
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get(*args, **kwargs)
    

class TaskList(LoginRequiredMixin, ListView):
    """
    View to display a list of tasks for the logged-in user.
    """
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        """
        Add additional context including count of incomplete tasks.
        """
        context = super().get_context_data(**kwargs)
        user_tasks = context['tasks'].filter(user=self.request.user)
        context['tasks'] = user_tasks
        context['count'] = user_tasks.filter(done=False).count()
        
        """
        Add search-area input for a diferent filter.
        """
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            user_tasks = context['tasks'].filter(title__startswith=search_input)
            context['tasks'] = user_tasks
        context['search-input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    """
    View to display details of a specific task.
    """
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    """
    View to handle creation of a new task.
    """
    model = Task
    fields = ['title', 'description', 'done']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        """
        Set the user of the task to the logged-in user.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    """
    View to handle updating an existing task.
    """
    model = Task
    fields = ['title', 'description', 'done']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    """
    View to handle deletion of a task.
    """
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
