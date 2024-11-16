from django.shortcuts import render, redirect
from .models import Obituary
from django.http import HttpResponse
from django.utils.text import slugify
def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        dod = request.POST['dod']
        content = request.POST['content']
        author = request.POST['author']
        slug = slugify(name)  
        obituary = Obituary(
            name=name,
            date_of_birth=dob,
            date_of_death=dod,
            content=content,
            author=author,
            slug=slug
        )
        obituary.save()

        return HttpResponse("Obituary submitted successfully!")
    return render(request, 'obituaries/obituary_form.html')
