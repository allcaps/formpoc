from django.views.generic import FormView
from bs4 import BeautifulSoup

from webapp.forms import ContactForm
from django.http import HttpResponse


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "webapp/contact.html"
    success_url = "/success/"

    def post(self, request, *args, **kwargs):
        response = super(ContactFormView, self).post(request, *args, **kwargs)
        elm_id = request.GET.get("elm_id")
        if elm_id:
            elm = BeautifulSoup(response.render().content, "html.parser").find(id=elm_id)
            return HttpResponse(elm)
        return response
