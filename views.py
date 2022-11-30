from django.db.models import Q
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect, reverse

from core import models
from plugins.liquidxslt import forms, logic
from security import decorators


@decorators.has_journal
@staff_member_required
def manager(request):
    xsl_files = models.XSLFile.objects.all()
    if request.journal:
        xsl_files = xsl_files.filter(
            Q(journal=request.journal)
            | Q(journal__isnull=True)
        )

    if request.POST:
        xsl_file_id = request.POST.get('new')
        xsl_file = get_object_or_404(
            models.XSLFile,
            pk=xsl_file_id,
        )
        logic.generate_child_xsl(
            request.journal,
            old_file=xsl_file,
        )

    template = 'liquidxslt/manager.html'
    context = {
        'xsl_files': xsl_files,
    }

    return render(request, template, context)


@decorators.has_journal
@staff_member_required
def edit_xslt_file(request, xsl_file_id):
    xsl_file = get_object_or_404(
        models.XSLFile,
        pk=xsl_file_id,
    )
    form = forms.XSLForm(
        instance=xsl_file,
    )
    if request.POST:
        form = forms.XSLForm(
            request.POST,
            instance=xsl_file,
        )
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.INFO,
                "XSLT file saved"
            )
            return redirect(
                reverse(
                    'liquidxslt_edit_xslt_file',
                    kwargs={'xsl_file_id': xsl_file.pk}
                )
            )
    template = 'liquidxslt/edit_xslt_file.html'
    context = {
        'xsl_file': xsl_file,
        'form': form,
    }
    return render(request, template, context)
