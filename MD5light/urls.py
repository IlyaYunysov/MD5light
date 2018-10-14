from django.conf.urls import url
from core.views import submit, check

urlpatterns = [
    url(r'^submit', submit),
    url(r'^check', check),
]
