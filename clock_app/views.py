from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def clock_view(request):
    return render(request, 'clock.html')
def clock_view(request):
    return render(request, 'clock.html')
def clock_view(request):
    return render(request, 'clock.html')
def clock_view(request):
    return render(request, 'clock.html')
def clock_view(request):
    return render(request, 'clock.html')
