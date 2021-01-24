from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpRequest

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })