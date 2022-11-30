from django import forms

from core import models
from plugins.liquidxslt import widgets


class XSLForm(forms.ModelForm):
    class Meta:
        model = models.XSLFile
        fields = ("label", "comments")

    xsl = forms.CharField(
        widget=widgets.CodeEditor,
    )

    def __init__(self, *args, **kwargs):
        super(XSLForm, self).__init__(*args, **kwargs)
        if self.instance:
            with open(self.instance.file.path) as xsl_file:
                xsl = xsl_file.read()
                self.fields['xsl'].initial = xsl

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        xsl = self.cleaned_data['xsl']
        with open(instance.file.path, 'w') as xsl_file:
            xsl_file.write(xsl)
            xsl_file.close()
