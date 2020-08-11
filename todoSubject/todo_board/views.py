from django.shortcuts import render
from django.views import generic
from .models import TodoList

# Create your views here.
class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_board_list.html'
        todo_list = TodoList.objects.all()
        return render(request, template_name, {"todo_list":todo_list})
