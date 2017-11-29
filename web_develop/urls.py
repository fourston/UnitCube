from django.conf.urls import url, include
from web_develop import views

app_name = 'web_develop'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # the 'name' value as called by the {% url %} template tag
]
