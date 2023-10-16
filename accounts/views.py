from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import View

User = get_user_model()

class SinginView(View):
    template_name = 'login.html'
    context = {}

    def get(self,request):
        return render(request, self.template_name)


    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Userneme or password invalid")
            return redirect('/accounts/login')


class RegisterView(View):
    template_name = 'register.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name)


    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username alredy exists!!")
                return redirect('/accounts/register')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email alredy exists!!!")
                return redirect('/accounts/register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1
                )
                user.save()
                return redirect('/accounts/login')
        else:
            messages.error(request, "Passwords is not same!!!")
            return redirect('/accounts/register')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')