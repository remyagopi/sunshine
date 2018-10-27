from django.shortcuts import render, Http404

# Create your views here.
def BlogHome(request):
    # if not request.user.is_authenticated:
    #     raise Http404
    return render(request,'home.html')