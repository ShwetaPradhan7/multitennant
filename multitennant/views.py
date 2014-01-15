from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
import re

from multitennantapp.models import sciences

def response(request):
    GETRequest = request.GET
    name_space = request.META['HTTP_NAME_SPACE']
    #print(request)
    subject = 'invalid'
    if name_space in 'math':
        subject = 'math'
        color = '#9999FF'
    if name_space in 'science':
        subject = 'science'
        color = '#99FF99'
    result = {}
    results = []
    for textdata in sciences.objects:
        if subject in textdata.text:
            #result = result + textdata.user['name'] + textdata.text
            result= {'name': textdata.user['name'], 'text': textdata.text}
            results.append(result) 
    t = loader.get_template('sciences.html')
    c = Context({'result' : results, 'title': subject, 'color': color})
    return HttpResponse(t.render(c))
