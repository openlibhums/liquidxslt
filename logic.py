import os

from django.template.loader import render_to_string
from django.conf import settings


def generate_child_xsl(journal, filename, old_file, new_file):
    context = {
        'old_file': old_file,
        'new_file': new_file,
    }
    new_file_contents = render_to_string(
        template_name='liquidxslt/child.xsl',
        context=context,
    )
    path = os.path.join(
        settings.BASE_DIR,
        'files',
        'xsl',
        'journals',
        str(journal.pk),
        filename,
    )
    with open(path, 'w') as file:
        file.write(new_file_contents)

    new_file.file.name = path
    new_file.save()
