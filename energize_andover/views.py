from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from energize_andover.forms import DocumentForm
from energize_andover.lib.file_transfer import transform_and_respond
from django.core.urlresolvers import reverse

def index(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            return transform_and_respond(request)
    else:
        form = DocumentForm() # A empty, unbound form

    # Render list page with the documents and the form
    return HttpResponse(render(request, 'energize_andover/index.html',
                               context={'title': 'Metasys Parsing', 'form': form}))
