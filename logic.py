import os
import uuid

from django.template.loader import render_to_string
from django.conf import settings
from core import models


def generate_child_xsl(journal, old_file, filename=None):
    xsl_uuid = uuid.uuid4()
    if not filename:
        filename = '{}.xsl'.format(xsl_uuid)
    new_file = models.XSLFile.objects.create(
        label=xsl_uuid,
        comments='XSL file created based on {}'.format(old_file.label),
        original_filename=filename,
        journal=journal,
    )
    context = {
        'old_file': old_file,
        'new_file': new_file,
    }
    new_file_contents = render_to_string(
        template_name='liquidxslt/child.xsl',
        context=context,
    )
    folder_path = os.path.join(
        settings.BASE_DIR,
        'files',
        'xsl',
        'journals',
        str(journal.pk),
    )

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'w') as file:
        file.write(new_file_contents)

    new_file.file.name = file_path
    new_file.save()
    return new_file
