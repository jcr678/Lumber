from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.views.generic import View
#from .models import Album
from .forms import UserForm 

def index(request):
    #context = {}
    return HttpResponse('<h1> "sign up" </h1>')

class UserFormView(View):
    form_class = UserForm
    template_name = 'userLogin/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            #clean data/normalize
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active: 
                    login(request, user)
                    #request.user.username
                    return redirect('userLogin:index')
        return render(request, self.template_name, {'form': form})