from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

    def get_object(self):
        return self.request.user


user_detail_view = UserDetailView.as_view()
class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail")
    
    def get_object(self):
        return User.objects.get(username = self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail")


user_redirect_view = UserRedirectView.as_view()


from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Premium
from rest_framework import serializers
from rest_framework.response import Response


class PremiaSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(groups__name="manager"))
    amount = serializers.IntegerField()
    date = serializers.DateTimeField()


class ListPremiumsAPI(ListAPIView):
    queryset = Premium.objects.all()
    serializer_class = PremiaSerializer


class DevApiView(APIView):


    def get(self, request, format=None):
        print("test",request)
        return Response({"detail": "This request is under development"})
