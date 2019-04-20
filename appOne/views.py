from django.shortcuts import render
#from django.http import HttpResponse
#from appOne.models import User
from appOne.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'appOne/index.html')


def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR, FORM INVALID')

    return render(request, 'appOne/users.html',{'form':form})
