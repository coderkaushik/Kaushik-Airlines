from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        "variable":"Hello World"
    }
    # return HttpResponse('Hello World')
    return render(request,'index.html',context)

def contact(request):
    # return HttpResponse('This is Contact Page')
    return render(request,'contact.html')
def about(request):
    # return HttpResponse('This is about us page')
    return render(request,'about.html')