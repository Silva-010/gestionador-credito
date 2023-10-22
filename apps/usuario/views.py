from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import LoginForm

class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        # Personaliza el mensaje de error
        if not form.cleaned_data.get('username') or not form.cleaned_data.get('password'):
            form.add_error(None, 'Por favor complete ambos campos.')
        else:
            form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
        return super(Login, self).form_invalid(form)
    
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

