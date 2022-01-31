from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    recipients = forms.CharField()
    cc_myself = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        # self.helper.template_pack = "bootstrap5"
        self.helper.layout = Layout(
            "subject",
            "message",
            "sender",
            "recipients",
            "cc_myself",
        )

    def clean_recipients(self):
        data = self.cleaned_data['recipients']
        if "fred@example.com" not in data:
            # Field level validation (clean_recipients)
            raise ValidationError("You have forgotten about Fred! Add fred@example.com to recipients.")
        return data

    def clean(self):
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        # Validation is triggered on field blur.
        # The validation is only on the current field.
        # This means the following concepts need additional work:
        # - Fields that depend on each other
        # - Form level errors

        # if cc_myself and subject:
        #     # Only do something if both fields are valid so far.
        #     if "help" not in subject:
        #         # Form level validation (clean)
        #         raise ValidationError(
        #             "Did not send for 'help' in the subject despite "
        #             "CC'ing yourself."
        #         )

        if cc_myself and subject and "help" not in subject:
            msg = "Must put 'help' in subject when cc'ing yourself."
            # Form level (clean), with errors on fields
            self.add_error('cc_myself', msg)
            self.add_error('subject', msg)
