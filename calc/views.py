from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {'name':'kishan', 'surname':'sindhi'})

def add(request):
    val1 = int(request.GET['n1'])
    val2 = int(request.GET['n2'])
    res = val1+val2
    return render(request, 'result.html', {'result':res}) 

def name(request):
    fname = request.GET['fname']
    lname = request.GET['lname']
    return render(request, 'name.html', {'fname':fname, 'lname':lname})
