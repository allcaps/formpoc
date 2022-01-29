from django.urls import path

from webapp.views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name='home')
]