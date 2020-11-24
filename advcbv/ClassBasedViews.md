For most experienceddevelopers CVB are the first choice for writing views;

1- add (from django.views.generic import View);
2- exemple of CBV:

    class CBView(View):
     def get(self,request):
         return HttpResponse("CLASS BASED VIEWS ARE COOL")