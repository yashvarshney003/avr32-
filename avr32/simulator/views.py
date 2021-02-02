from django.shortcuts import render,HttpResponse


def index(request):
    return render(request,'index.html')
# Create your views here.
def assembler(request):
   if(request.method == "POST"):
       code = request.POST['code']
       print(code)
       return HttpResponse("<h1> code reciever</h1>")

   