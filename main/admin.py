from django.contrib import admin
from main.models import Mailing, Message, Client, Attempt

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'periodicity', 'author', 'message', 'clients')

    def	clients(self, row):
        return ','.join([x.clients for x in row.clients.all()])

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'content')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'author')


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'last_attempt', 'status', 'server_code')

