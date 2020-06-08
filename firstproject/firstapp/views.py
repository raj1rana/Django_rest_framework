from django.shortcuts import render
from django.http import JsonResponse
from firstapp.models import Employee
# Create your views here.
# simple view 
# def emplpyee(request):
#     employee = {
#         'id': 1,
#         'name': 'Jhon',
#         'salary': 100000

#     }
#     return JsonResponse(employee)

# returning model data as json obj
def emplpyee(request):
    data = Employee.objects.all()
    response = {
        'employeed': list(data.values('id', 'name', 'sal'))
    }
    return JsonResponse(response)