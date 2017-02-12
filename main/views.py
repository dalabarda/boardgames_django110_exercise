from django.shortcuts import render



def home(request):
    context = context={'message': 'Hello, World!'}
    template = "main/home.html"
    return render(request, template)
    # return render(request=request, template_name="main/home.html", context={'message': 'Hello, World!'})

# def home(request):
# 	return HttpResponse("Hello world!")