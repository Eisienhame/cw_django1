from django.shortcuts import render, get_object_or_404
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from main.models import Mailing, Client, Message
from main.forms import MailingForm, ClientForm
from main.services import send_manager


class HomeView(generic.TemplateView):
    template_name = 'main/homepage.html'

    def get_context_data(self, **kwargs):
        blog = Mailing.objects.order_by('?')[:3]
        clients_count = len(Client.objects.all())  # кол-во клиентов
        mailing_count = len(Mailing.objects.all())  # кол-во рассылок
        mailing_active = len(Mailing.objects.filter(status='LAUNCHED'))  # кол-во активных рассылок
        context = super().get_context_data()
        context['mailing_count'] = mailing_count
        context['mailing_active'] = mailing_active
        context['clients_count'] = clients_count
        context['blogs'] = blog

        return context

class MailingListView(LoginRequiredMixin, generic.ListView):
    model = Mailing


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Mailing
    permission_required = 'main.view_mailing'


class MailingCreateView(LoginRequiredMixin, generic.CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('main:mailing_list')
    #fields = ('name', 'send_time', 'start_date', 'end_date', 'periodicity', 'author')

    def form_valid(self, form):
        instance = form.save()
        instance.author = self.request.user

        send_manager()

        return super().form_valid(form)


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Mailing

    success_url = reverse_lazy('main:mailing_list')
    permission_required = 'main.delete_mailing'


class MailingUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'main/mailing_form.html'
    success_url = reverse_lazy('main:mailing_list')


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Client
    permission_required = 'main.view_client'


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:client_list')

    def form_valid(self, form):
        instance = form.save()
        instance.author = self.request.user
        return super().form_valid(form)

class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Client

    success_url = reverse_lazy('main:mailing_list')
    permission_required = 'main.delete_client'


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:client_list')


class MessageListView(LoginRequiredMixin, generic.ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Message
    permission_required = 'main.view_message'


class MessageCreateView(LoginRequiredMixin, generic.CreateView):
    model = Message
    success_url = reverse_lazy('main:message_list')
    fields = ('theme', 'content')

class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Message

    success_url = reverse_lazy('main:message_list')
    permission_required = 'main.delete_message'


class MessageUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Message
    success_url = reverse_lazy('main:message_list')