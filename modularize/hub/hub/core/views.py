from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, 'core/index.html', {'user': request.user})

def account_redirect(request):
    return redirect('index')