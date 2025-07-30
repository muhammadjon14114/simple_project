from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

class DashboardView(LoginRequiredMixin, View):
    login_url = '/login/'  # foydalanuvchi login qilmagan bo‘lsa shu yerga yuboriladi
    redirect_field_name = 'next'  # optional, default qiymat

    def get(self, request):
        return render(request, 'dashboard.html')
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # agar allaqachon login bo‘lgan bo‘lsa, to‘g‘ridan-to‘g‘ri dashboardga
    next_page = 'dashboard'             # login bo‘lgandan keyin qayerga boradi

    def form_invalid(self, form):
        messages.error(self.request, "Login yoki parol noto'g'ri.")
        return super().form_invalid(form)
    
class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            return redirect(reverse('dashboard'))
        return render(request, 'register.html', {'form': form})
