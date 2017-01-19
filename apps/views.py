from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.
from django.template import context
from django.template.context import RequestContext
from django.views.generic.base import View

from apps.forms import BiodataForm
from apps.serializers import UserSerializer


class Index(View):
    template_name = 'index.html'
    form_class = BiodataForm
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print(form.data)
            return HttpResponse(form.data['address'])
        else:
            error = form.errors
            print('error')
            #print(error)
            return render(request, self.template_name, {'error': error,'form': self.form_class})

        # return render(request, self.template_name,{'form': self.form_class})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer