from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse 
from . forms import Student_Rgistration
from . models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View


class UserAddShowView(TemplateView):

    template_name = 'App_Enroll/add-show.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = Student_Rgistration()
        objects = User.objects.all
        context = {'form': form, 'objects':objects}
        return context

    def post(self, request):
        form = Student_Rgistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            registration = User(name=name, email=email, password=password) #creating a object 
            registration.save()
        return HttpResponseRedirect(reverse('show_data'))

class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs): 
        delete_id = kwargs['id'] 
        User.objects.get(pk=delete_id).delete()
        return super().get_redirect_url(self, *args, **kwargs)
     
class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        form = Student_Rgistration(instance=pi)
        return render(request, 'App_Enroll/update-student.html', context={'form':form})  

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        form = Student_Rgistration(request.POST, instance=pi)
        if form.is_valid:
            form.save() 
        return HttpResponseRedirect(reverse('show_data'))       
 
