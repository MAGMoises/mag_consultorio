from django.shortcuts import render
from django.contrib import messages

def index(request):
    messages.debug(request, 'teste')
    messages.info(request, 'ok')
    messages.success(request, 'sucesso')
    messages.warning(request, 'Your account')
    messages.error(request, 'Document deleted.')

    return render(request, 'index.html')
    
