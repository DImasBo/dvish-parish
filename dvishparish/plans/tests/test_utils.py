import pytest

from django.test import TestCase
from mixer.backend.django import mixer
from dvishparish.plans import utils
from django.utils import timezone
from datetime import datetime, timedelta

pytestmark = pytest.mark.django_db

class TestUtils(TestCase):
    def setUp(self):
        
        today = timezone.now()
        t_delta = timedelta(days=5)
        date_from = today - t_delta
        date_to = today + t_delta

        self.bankoffice = mixer.blend("users.BankOffice")
        self.users = mixer.cycle(3).blend("users.User", amount=5000, bankoffice=self.bankoffice)

        print(self.users)
       
        self.kpi = mixer.blend("plans.KPI",)
        
        self.general_plan = mixer.blend("plans.GeneralPlan", date_from=date_from, date_to=date_to, kpi=self.kpi)
       
        self.manager_plan = mixer.blend("plans.ManagerPlan", user=self.users[0], amount=5000,general_plan=self.general_plan)
        self.manager_plan = mixer.blend("plans.ManagerPlan", user=self.users[1], amount=5000,general_plan=self.general_plan)
        self.manager_plan = mixer.blend("plans.ManagerPlan", user=self.users[2], amount=5000,general_plan=self.general_plan)

    def test_get_kpi_daily(self):
        plans = utils.get_kpi_daily(self.manager_plan)
        # print(self.manager_plan)
        # print(self.manager_plan.general_plan)
        # print(plans)
        assert 1 == 2

    def test_get_сurrent_manager_plans(self):
        plans = utils.get_сurrent_manager_plans(self.manager_plan.user)

        assert plans.count() == 1

    def test_get_current_bankoffice_plans(self):
        plans = utils.get_current_bankoffice_plans(self.manager_plan.user)

        assert 2== 1