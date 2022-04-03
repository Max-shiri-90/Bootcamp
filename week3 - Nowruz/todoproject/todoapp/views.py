from django.shortcuts import render


def todoapp_view(request):
    return render(request, 'todolist.html')
