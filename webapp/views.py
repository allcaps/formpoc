from django.http import JsonResponse
from django.views.generic import FormView

from webapp.forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "webapp/contact.html"
    success_url = "/success/"

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = self.form_class(request.POST)
        form.is_valid()
        errors = form.errors.get(field_name, [])
        return JsonResponse({
            "__field_name__": field_name,
            "errors": errors,
        })
