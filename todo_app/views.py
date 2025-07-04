from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_http_methods


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@login_required
@require_http_methods(["GET", "POST"])
def task_list_view(request):
    if request.method == "POST":
        Task.objects.create(
            user=request.user,
            title=request.POST['title'],
            description=request.POST.get('description', ''),
            priority=request.POST['priority'],
            category=request.POST['category'],
            due_date=request.POST['due_date'],
        )
        return redirect('task_list')

    tasks = Task.objects.filter(user=request.user)

    # Filters
    priority = request.GET.get('priority')
    category = request.GET.get('category')
    completed = request.GET.get('completed')

    if priority:
        tasks = tasks.filter(priority=priority)
    if category:
        tasks = tasks.filter(category=category)
    if completed in ['true', 'false']:
        tasks = tasks.filter(completed=(completed == 'true'))

    tasks = tasks.order_by('-created_at')
    return render(request, 'todo_app/task_list.html', {'tasks': tasks})


@login_required
@require_http_methods(["POST"])
def mark_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')


@login_required
@require_http_methods(["POST"])
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')
