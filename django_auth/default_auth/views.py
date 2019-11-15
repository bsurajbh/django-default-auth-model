from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages


class SignupView(FormView):
    template_name = 'default_auth/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('default_auth:dashboard')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()

        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())


def Dashboard(request):
    return render(request, 'default_auth/dashboard.html')


def Logout(request):
    """logout logged in user"""
    logout(request)
    return redirect(reverse_lazy('default_auth:dashboard'))


class LoginView(FormView):
    """ login view"""
    template_name = 'default_auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('default_auth:dashboard')

    def form_valid(self, form):
        post_data = form.cleaned_data
        user = authenticate(username=post_data['username'],
                            password=post_data['password'])
        if user is not None:
            login(self.request, user)
        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials.\
                    Please try again with correct input')
            return HttpResponseRedirect(reverse_lazy('default_auth:login'))

        return HttpResponseRedirect(reverse_lazy('default_auth:dashboard'))
