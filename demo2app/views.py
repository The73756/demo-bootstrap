from django.contrib.auth import login
from django.contrib.auth.mixins import *
from django.contrib.auth.views import LoginView, UserModel
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView

from demo2app.forms import *
from demo2app.models import *


# Create your views here.
class RequestListView(ListView):
    model = Request
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return ''

        if self.request.user.is_staff:
            return Request.objects.all()
        else:
            return Request.objects.filter(user=self.request.user)


class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomRegistrationView(CreateView):
    model = UserModel
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        phone = form.cleaned_data['phone']
        patronymic = form.cleaned_data['patronymic']
        Profile.objects.create(user=user, phone=phone, patronymic=patronymic)

        login(self.request, user=user)
        return redirect(self.success_url)


class CreateRequestView(LoginRequiredMixin, CreateView):
    model = Request
    template_name = 'create-request.html'
    form_class = CreateRequestForm
    success_url = '/'

    def form_valid(self, form):
        new_request = form.save(commit=False)
        new_request.user = self.request.user

        return super(CreateRequestView, self).form_valid(form)


class AdminRequestsView(PermissionRequiredMixin, ListView):
    model = Request
    permission_required = 'is_stuff'
    template_name = 'site-admin/index.html'

    def handle_no_permission(self):
        return redirect('/')

    def get_queryset(self):
        if not self.request.user.is_staff:
            return redirect('/')
        return Request.objects.all()


class EditRequestView(PermissionRequiredMixin, UpdateView):
    model = Request
    permission_required = 'is_stuff'
    template_name = 'site-admin/edit.html'
    success_url = '/site-admin'
    fields = ['address',
              'date',
              'phone',
              'status',
              'reject_message']

    def handle_no_permission(self):
        return redirect('/')
