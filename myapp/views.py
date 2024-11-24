from django.shortcuts import render




# Create your views here.
def index(request):
    return render(request , 'index.html')
def trainer(request):
    return render(request , 'trainer.html')