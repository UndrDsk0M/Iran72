from django.shortcuts import render, HttpResponse
from .models import word_tr
from django.shortcuts import get_object_or_404
# Create your views here.

def finding_word(request):
    quary = request.GET.get('q', '')
    word = get_object_or_404(word_tr, word_pr=quary )
    print(quary)
    return HttpResponse(word)

