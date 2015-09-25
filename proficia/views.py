from django.http import HttpResponse
from django.shortcuts import render


def editingpage(request):
    return render(request, "editing.html", {})