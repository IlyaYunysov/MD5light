from django.db import models
import uuid
from .task import get_md5_task, send_mail_task
from django.dispatch import receiver


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=254, blank=True)
    url = models.URLField(blank=True)
    md5 = models.CharField(max_length=32, blank=True)
    status = models.CharField(max_length=10, default='running')


@receiver([models.signals.post_save], sender=Task, dispatch_uid="my_unique_identifier")
def task_post_create(sender, instance, signal, *args, **kwargs):
    if instance.status == 'running':
        get_md5_task.delay(instance.id)
    if instance.status == 'done' and instance.email:
        send_mail_task.delay(instance.id)
