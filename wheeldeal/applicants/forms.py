from django import forms

from wheeldeal.applicants.models import Applicant
from wheeldeal.mixins.BootstrapMixins.FormControlMixin import FormControlMixin


class ApplyForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('front_side_id_image', 'back_side_id_image')