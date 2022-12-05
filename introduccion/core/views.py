from django.views.generic import View
from django.shortcuts import render

#vista de clases 
class HomeView(View):
    #args y kwargs son para ver parametros CUALQUIER
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'index.html', context)