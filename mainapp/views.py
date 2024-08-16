from django.shortcuts import render
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse

def index_view(request):
    return render(request, 'mainapp/index.html')


def about_view(request):
    return render(request, 'mainapp/about.html')

@csrf_protect
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm2(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm2()
    context = {'form': form}
    return render(request, 'mainapp/contact.html', context)

@csrf_protect
def test_view(request):
    if request.method == 'POST':
        # first way to insert in DB (Form)
        # form = ContactForm1(request.POST)
        # if form.is_valid():
        #     name = form.cleaned_data['name']
        #     email = form.cleaned_data['email']
        #     subject = form.cleaned_data['subject']
        #     message = form.cleaned_data['message']
        #     c = Contact(name=name, email=email, subject=subject, message=message)
        #     c.save()
        # end first way

        # second way to insert in DB (Model Form)
        form = ContactForm2(request.POST)
        if form.is_valid():
            form.save()
        # end second way

            return HttpResponse('success')
        else:
            return HttpResponse('not_valid')

    form = ContactForm2()
    context = {'form': form}
    return render(request, 'mainapp/test.html', context)