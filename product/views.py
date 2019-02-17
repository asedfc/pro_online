from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.

class Onsale(View):
    def dispatch(self, request, *args, **kwargs):
        print('before')
        obj = super(Onsale, self).dispatch(request, *args, **kwargs)
        print('after')
        return obj

    def get(self, request, pro_id):
        print(pro_id)
        return render(request, 'onsale.html')

    def post(self, request):
        print(request.POST.get('user'))
        return HttpResponse('Login.post')
    