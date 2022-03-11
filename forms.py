from django import forms

from plugins.liquidxslt import widgets


class XSLForm(forms.Form):
    xsl = forms.CharField(
        widget=widgets.CodeEditor,
    )

    def __init__(self, *args, **kwargs):
        self.xsl_file = kwargs.pop('xsl_file', None)
        super(XSLForm, self).__init__(*args, **kwargs)
        with open(self.xsl_file.file.path) as xsl_file:
            xsl = xsl_file.read()
            self.fields['xsl'].initial = xsl

    def save(self):
        xsl = self.cleaned_data['xsl']
        with open(self.xsl_file.file.path, 'w') as xsl_file:
            xsl_file.write(xsl)
            xsl_file.close()
