from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service, Portfolio, Testimonial

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'web_develop/index.html'
    context_object_name = 'services_list'

    def get_queryset(self):
        return Service.objects.filter().order_by('sort_index')[:6]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet
        context['portfolio_list'] = Portfolio.objects.filter().order_by('sort_index')[:10]
        context['testimonial_list'] = Testimonial.objects.all() #надо рандомизировать отзывы скорее всего, подумать
        return context
