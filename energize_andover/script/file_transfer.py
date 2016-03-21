from django.http import HttpResponse
from mysite.settings import BASE_DIR
from energize_andover.script.parse import parse, summarize, save_df
import os

def save(form_data):
    uploaded_file = form_data['metasys_file']
    uploaded_filename = uploaded_file.name
    full_filename = os.path.join(BASE_DIR, uploaded_filename)

    with open(full_filename, 'wb') as fout:
        for chunk in uploaded_file.chunks():
            fout.write(chunk)

    return full_filename

def transform_and_save(form_data):
    original_saved_filename = save(form_data)
    df = parse(original_saved_filename)
    if form_data['summarize']:
        df = summarize(df, .12)
    transformed_saved_filename = original_saved_filename + '_transformed'
    save_df(df, form_data['summarize'], None, None, transformed_saved_filename)

    return transformed_saved_filename

def transform_and_respond(form_data):
    transformed_saved_filename = transform_and_save(form_data)

    transformed_saved_file = open(transformed_saved_filename).read()
    response = HttpResponse(transformed_saved_file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="%s"' % transformed_saved_filename

    return response
