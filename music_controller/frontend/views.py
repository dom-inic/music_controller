from django.shortcuts import render

# Create your views here.

def base(request):
    """ homepage """
    template_name = 'frontend/index.html'
    return render (request, template_name)

# def objects(request):
#     """ dict test """
#     cars = Cars.objects.all()
#     context = {
#         "cars": def f

#     }


