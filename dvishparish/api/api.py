from django.urls import path, include
from dvishparish.users.models import User, Premium, Bonus
from dvishparish.manager_roles.models import ResultDaily
from rest_framework import routers, serializers, viewsets, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url","id", "integration_id", 'username', 'email', "first_name" ,"last_name",]# "bankoffice", "results_daily"]


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.filter(groups__name="manager")
    serializer_class = UserSerializer


class PremiusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Premium
        fields = ["url",'id', 'user_id', "user", "amount", "date"]


class PremiumViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    permission_classes = [IsAuthenticated]

    queryset = Premium.objects.all()
    serializer_class = PremiusSerializer


class BonusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Premium
        fields = ["url",'id', 'user_id',"user", "amount", "date"]


class BonusViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    permission_classes = [IsAuthenticated]
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    results_items = serializers.StringRelatedField(many=True)
    class Meta:
        model = ResultDaily
        fields = ["url",'id', 'user_id', "user", "results_items"]


class ResultDailyViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    permission_classes = [IsAuthenticated]
    queryset = ResultDaily.objects.all()
    serializer_class = ResultSerializer


class ResultDailyAPI(CreateAPIView):
    queryset = ResultDaily.objects.all()
    serializer_class = ResultSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'premius', PremiumViewSet)
router.register(r'bonus', BonusViewSet)
router.register(r'result', ResultDailyViewSet)
# router.register(r'result_create', ResultDailyAPI.)
