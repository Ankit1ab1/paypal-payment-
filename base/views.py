from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def store(request):
    if request.method=='POST':
    		return render(request, 'base/simple_checkout.html',{'amount':request.POST.get('amount')})
    return render(request, 'base/store.html')

