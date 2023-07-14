from django.contrib import admin
from main.models import Mailing, Message, Client

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'periodicity')



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'theme')



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'mailings')

    def	mailings(self, row):
        return ','.join([x.mailing for x in row.mailings.all()])


