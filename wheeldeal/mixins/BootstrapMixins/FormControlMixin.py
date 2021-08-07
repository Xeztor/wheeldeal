class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._add_form_control_to_fields()

    def _add_form_control_to_fields(self):
        for _, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                continue

            field.widget.attrs['class'] += ' form-control'