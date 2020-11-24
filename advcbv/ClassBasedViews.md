For most experienceddevelopers CVB are the first choice for writing views;

1- add (from django.views.generic import View);
2- exemple of CBV:

    class CBView(View):
     def get(self,request):
         return HttpResponse("CLASS BASED VIEWS ARE COOL")

    
FUNCTION BASED VIEW:

    def index(request):
        return render(request,'index.html')

CLASS BASED TEMPLATE VIEW:

    class IndexView(TemplateView):
        template_name = 'index.html'

TemplateView:

    We need to import TemplateView from django.views.generic to the views.py file

