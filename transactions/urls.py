from django.conf.urls import url

from .views import deposit_view, withdrawal_view
from transactions import views


app_name = 'transactions'

urlpatterns = [
    # url(r'^$', home_view, name='home'),
    url(r'^deposit/$', deposit_view, name='deposit'),
    url(r'^withdrawal/$', withdrawal_view, name='withdrawal'),
    url('contact/',views.contact,name="contact"),
    url('chatbot/',views.chatbot,name="chatbot"),
    url('loan/',views.loan,name="loan"),
     url('atm/',views.atm,name="atm")
]
