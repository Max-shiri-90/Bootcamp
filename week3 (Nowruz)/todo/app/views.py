from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

from .models import Todo


def todo_list(request):
    todo_qs: Todo = Todo.objects.all()
    result = []

    for elm in todo_qs:
        result.append({
            "user": elm.user.username,  # in query behineh nist, felan savademun nareside be join ---> select_related
            "title": elm.title,
            "due_date": elm.due_date,
            "done": elm.done,
            "description": elm.description
        })
    return JsonResponse(result, safe=False)


def todo_detail(request, username):
    """
    faghat task user mored nazar ra midahad
    """
    user_obj = get_object_or_404(User, username__exact=username)
    todo_qs: Todo = Todo.objects.filter(user__username__exact=username)
    # todo_qs = user_obj.todos.all() #related_name
    result = []
    for elm in todo_qs:
        result.append({
            "user": elm.user.username,  # in query behineh nist, felan savademun nareside be join ---> select_related
            "title": elm.title,
            "due_date": elm.due_date,
            "done": elm.done,
            "description": elm.description
        })
    return JsonResponse(result, safe=False)


def todo_search(request):
    pass
