from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'fm100/index.html')


def aboutfm100(request):
    return render(request, 'fm100/aboutfm100.html')


def testpage(request):
    return render(request, 'fm100/testpage.html')

def loginpage(request):
    return render(request, 'fm100/login.html')
