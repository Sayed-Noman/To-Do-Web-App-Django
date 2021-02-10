from django.shortcuts import render
from django.http import HttpResponse

# todolist/Homepage View
def todolist(request):
    context={
        'welcome_text':"Welcome to Taskmate...",
    }
    return render(request, 'todolist.html',context)

# Contact Page View
def contact(request):
    context={
        'contact_text':"For Further Information Contact Us!",
    }
    return render(request,'contact.html',context)

# About us Page View
def about(request):
    context={
        'about_text':"Want to Know about Us?",
    }
    return render(request,'about.html',context)
 