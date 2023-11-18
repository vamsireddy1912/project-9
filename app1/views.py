from django.shortcuts import render

# Create your views here.
def data_render(request):
    data  = 'this data is just an assumption'
    d = {'whatever': data}
    return render(request,'data_render.html', context=d)