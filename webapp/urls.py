from django.urls import path

from webapp.views import ContactFormView

app_name = "webapp"

urlpatterns = [
    path('', ContactFormView.as_view(), name='home')
]