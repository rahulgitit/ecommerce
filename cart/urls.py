"""cart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from enroll import views
from enroll.views import profileviewclass
from enroll.forms import setpasswordconfirm
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordChangeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home , name="home"),
    path("search", views.search , name="search"),
    path("checkout/", views.checkout, name="checkout"),
    path("paymentdone", views.payment_done, name="paymentdone"),
    path("order/", views.order, name="order"),
    # path("profile/", views.profile, name="profile"),
    path("profile/", profileviewclass.as_view(), name="profile"),

    path("address/", views.address, name="address"),

    path("product_details/<int:pk>",views.product_details, name="product_details"),
    path("add_to_cart", views.addtocart, name="add_to_cart"),
    path('cart', views.show_cart, name="cart"),
    path("login/",views.log_in, name="login"),
    path("signup/",views.singuppage, name="signup"),
    path("logout/",views.log_out, name="logout"),
    # path("password_change/",views.password_changeform, name="password_change"),
    path("password_change/", PasswordChangeView.as_view(template_name="password_change.html",form_class=setpasswordconfirm), name="password_change"),
    path("password_reset/", PasswordResetView.as_view(template_name = "passwordreset.html"), name="password_reset"),
    path("password_reset_done/",PasswordResetDoneView.as_view(template_name="passwordresetdone.html"), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/",PasswordResetConfirmView.as_view(template_name="passwordresetconfirm.html", form_class=setpasswordconfirm), name="password_reset_confirm"),
    path("password_reset_complete/",PasswordResetCompleteView.as_view(template_name="passwordresetcomplete.html"), name="password_reset_complete"),

    path("top/", views.topwear, name="topwear"),
    path("api/", include('enroll.api.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)