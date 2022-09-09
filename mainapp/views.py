import re
from urllib import response
from django.shortcuts import render
from .mainbot import get_response

def bot (request):
    # message = 'Hello k cha'
    message = 'Ask me anything'
    return render(request, 'index.html', {'message':message} )


from django.http import JsonResponse
def botreply(request):
    msg = request.POST.get('msg')
    print(msg)
    message = get_response(msg)
    return JsonResponse({'botreply':message})