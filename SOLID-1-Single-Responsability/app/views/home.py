from django.shortcuts import render

class Home:
    def home(request):
        template = 'home.html'
        return render(request, template)