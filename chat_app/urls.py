from django.urls import path, include
from chat_app import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        request.session.flush()
        return super().dispatch(request, *args, **kwargs)
    
class CustomLoginView(LoginView):
    def form_valid(self, form):
        # Clear any existing session data
        self.request.session.flush()
        # Call the parent form_valid method to log the user in
        return super().form_valid(form)

urlpatterns = [
    path("", chat_views.chat, name="chat-page"),
    # login-section
    path("auth/login/", CustomLoginView.as_view
         (template_name="chat_app/login.html"), name="login-user"),
    path("auth/logout/", CustomLogoutView.as_view(), name="logout-user"),
]