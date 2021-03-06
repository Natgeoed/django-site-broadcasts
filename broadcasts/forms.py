from django import forms
from django.utils.translation import ugettext_lazy as _

from broadcasts.models import BroadcastMessage


class BroadcastMessageForm(forms.ModelForm):
    """
    Allows custom validation of admin input
    """

    class Meta:
        model = BroadcastMessage
        fields = '__all__'

    def clean(self):
        """
        Ensure that the start time precedes the end time
        """
        cleaned_data = self.cleaned_data
        start_time = cleaned_data["start_time"]
        end_time = cleaned_data["end_time"]
        if start_time >= end_time:
            raise forms.ValidationError(
                _("The start time must come before the end time"))
        return cleaned_data
