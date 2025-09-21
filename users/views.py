from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import userForm

# Create your views here.

def homeview(request):
    return render(request,'home.html',{})

class LoginView(TemplateView):
    template_name = 'users/loginform.html'
    form_class = userForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        return render(request,self.template_name,{'form':form})