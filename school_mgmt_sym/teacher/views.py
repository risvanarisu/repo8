from django.shortcuts import render

# Create your views here.
def registerteachers(request):
    return render(request,"teachers/addteacher.html")

def getteachers(request):
    return render(request,"teachers/displayteacher.html")