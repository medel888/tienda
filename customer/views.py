from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.urls import reverse_lazy
from store.views import all_products

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('store/home.html')  # Cambia 'nombre_vista' por el nombre de la vista a la que deseas redirigir después del inicio de sesión
    else:
        form = AuthenticationForm()
    return render(request, 'customer/login.html', {'form': form})

