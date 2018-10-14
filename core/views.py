from django.views.decorators.csrf import csrf_exempt
from .models import Task
from django.http.response import JsonResponse
from django.core.exceptions import ValidationError


@csrf_exempt
def submit(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
        except Exception:
            email = ''
        task = Task.objects.create(
            email=email,
            url=request.POST['url']
        )
        return JsonResponse({'id': task.id})


def check(request):
    if request.method == 'GET':
        try:
            task_id = request.GET.get('id')
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return JsonResponse({'status': 'missing'})
        except ValidationError:
            return JsonResponse({'status': 'missing'})
        if task.status == 'done':
            response = {
                'md5': task.md5,
                'status': task.status,
                'url': task.url,
            }
        else:
            response = {
                'status': task.status
            }
        return JsonResponse(response)
