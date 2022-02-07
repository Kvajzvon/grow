from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.views import send_verification_email
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from media_handler.models import Post

# Create your views here.

@login_required
def dashboard_view(request):          
    context = {}

    user = request.user

    context['user'] = user
    context['recommended'] = Post.get_recommended_posts(user, amount=9)
    context['continue'] = Post.get_user_history(user).first()
    
    if not request.user.is_validated:
        return redirect("core:unvalidated") # TODO: greg
    
    return render(request, "core/dashboard.html", context)

@login_required
def unvalidated_view(request):
    context = {}
    context['user'] = request.user
    
    if request.user.is_validated:
        return redirect("core:dashboard")
    
    if request.POST:
        if "resend_verification" in request.POST:
            send_verification_email(request, request.user)
            messages.info(request, _("Validation email has been sent"))
    
    return render(request, "core/unvalidated.html", context)

def error_404_view(request):
    return render(request, "core/errors/404.html")

def cookie_view(request):
    return render(request, "core/cookielaw.html")