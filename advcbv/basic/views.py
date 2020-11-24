# We add this
from django.views.generic import View, TemplateView

# Create your views here.

#def index(request):
 #   return render(request,'index.html')

#class CBView(View):
 #    def get(self,request):
  #       return HttpResponse("CLASS BASED VIEWS ARE COOL")

class IndexView(TemplateView):
        template_name = 'index.html'