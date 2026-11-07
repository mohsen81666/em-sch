from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')


def educators(request):
    return render(request, 'pages/educators.html')


def honors(request):
    return render(request, 'pages/honors.html')


def gallery(request):
    return render(request, 'pages/gallery.html')


def videos(request):
    return render(request, 'pages/videos.html')


def contact(request):
    return render(request, 'pages/contact.html')