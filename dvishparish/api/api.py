from django.urls import path, include
from dvishparish.users.models import User, Premium, Bonus
from dvishparish.manager_roles.models import ResultDaily
from rest_framework import routers, serializers, viewsets, generics


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # bankoffice = serializers.StringRelatedField()
    # results_daily = serializers.StringRelatedField(many=True)

    # results_daily = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ["url","id", "integration_id", 'username', 'email', "first_name" ,"last_name",]# "bankoffice", "results_daily"]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name="manager")
    serializer_class = UserSerializer


class PremiusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Premium
        fields = ["url",'id', 'user_id', "user", "amount", "date"]

class PremiumViewSet(viewsets.ModelViewSet):
    queryset = Premium.objects.all()
    serializer_class = PremiusSerializer

class BonusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Premium
        fields = ["url",'id', 'user_id',"user", "amount", "date"]

class BonusViewSet(viewsets.ModelViewSet):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    results_items = serializers.StringRelatedField(many=True)
    class Meta:
        model = ResultDaily
        fields = ["url",'id', 'user_id', "user", "results_items"]

from rest_framework.generics import CreateAPIView

class ResultDailyViewSet(viewsets.ModelViewSet):
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
