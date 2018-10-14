from MD5light.celery import app
import hashlib
from urllib.request import urlopen
from urllib.error import URLError
from django.apps import apps
from django.core.mail import send_mail
from MD5light.settings import EMAIL_HOST_USER
import ssl
import json


@app.task()
def get_md5_task(task_id):
    Model = apps.get_model(app_label='core_old', model_name='Task')
    task = Model.objects.get(id=task_id)
    try:
        cxt = ssl._create_unverified_context()
        file = urlopen(task.url, context=cxt).read()
        m = hashlib.md5()
        m.update(file)
        task.md5 = m.hexdigest()
        task.status = 'done'
    except URLError:
        task.status = 'failed'
    finally:
        task.save()


@app.task()
def send_mail_task(task_id):
    Model = apps.get_model(app_label='core_old', model_name='Task')
    task = Model.objects.get(id=task_id)
    message = {
        'md5': task.md5,
        'url': task.url,
    }
    send_mail('MD5 hash', json.dumps(message), EMAIL_HOST_USER,
              [task.email], fail_silently=False)