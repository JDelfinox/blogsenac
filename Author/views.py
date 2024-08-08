from django.shortcuts import render

def contato(request):
    return render(request, 'contact.html')

def post1(request):
    return render(request, 'post1.html')

def post2(request):
    return render(request, 'post2.html')

def post3(request):
    return render(request, 'post3.html')

def post4(request):
    return render(request, 'post4.html')
