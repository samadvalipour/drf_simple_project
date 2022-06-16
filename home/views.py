from django.http import HttpResponse
from django.views import View

class HomeView(View):
    def get(self,request):
        return HttpResponse("<h1>this is home</h1>")

