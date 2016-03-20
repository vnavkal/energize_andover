from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    title = 'Metasys Parsing'
    context = {'title': title, 'choices': ('a', 'b')}
    return HttpResponse(render(request, 'energize_andover/index.html', context))

def choose(request):
    return HttpResponse('you made a choice')
    # return HttpResponseRedirect('energize_andover/display_choice')

def display_choice(request):
    title = 'Here is your choice:'
    context = {'title': title, 'value': 'asdf'}
    return HttpResponse(render(request, 'energize_andover/display_choice.html', context))
