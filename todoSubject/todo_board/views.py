from django.shortcuts import render, redirect
from django.views import generic

# Create your views here.
class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_board_list.html'
        return render(request, template_name)
