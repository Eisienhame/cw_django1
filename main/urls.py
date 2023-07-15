from django.urls import path
from main.apps import MainConfig
from django.views.decorators.cache import cache_page
from main.views import HomeView, MailingListView, MailingCreateView, MailingDeleteView, MailingDetailView, \
    MailingUpdateView, ClientListView, ClientCreateView, ClientDeleteView, ClientDetailView, ClientUpdateView, \
    MessageUpdateView, MessageDetailView, MessageDeleteView, MessageCreateView, MessageListView, deactive_mailing

app_name = MainConfig.name

urlpatterns = [

    path('', HomeView.as_view(), name='homepage'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing_list/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_list/delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing_list/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_list/update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_list/create/', ClientCreateView.as_view(), name='client_create'),
    path('client_list/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('client_list/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_list/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_list/create/', MessageCreateView.as_view(), name='message_create'),
    path('message_list/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('message_list/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_list/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('detail/deactive_mailing/<int:pk>/', deactive_mailing, name='deactive_mailing'),

]