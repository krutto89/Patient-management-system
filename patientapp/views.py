from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'patientapp/index.html')

def about(request):
    return render(request,'patientapp/about.html')

def contact(request):
    return render(request,'patientapp/contact.html')