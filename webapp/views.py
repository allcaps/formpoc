from django.views.generic import FormView

from webapp.forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = "webapp/contact.html"
    success_url = "/#success"
