from django.shortcuts import render, HttpResponse

# Create your views here.
def firstpage(request):
    return HttpResponse("<h1 style='color: #AE6A0B; direction: rtl;text-align: center;padding: 40vh;font-size: xxx-large;'><b>به زودی...!</b></h1>")