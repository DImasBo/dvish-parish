import pytest

from django.test import TestCase
from mixer.backend.django import mixer
from dvishparish.utils.plans import get_сurrent_manager_kpis
from dvishparish.utils.result import get_sum_result_by_KPI_and_user
from django.utils import timezone
from datetime import datetime, timedelta

pytestmark = pytest.mark.django_db


class TestUtils(TestCase):
    def setUp(self):
        self.today = timezone.now()
        self.date_delta = timedelta(days=15)
        self.date_from = self.today - self.date_delta
        self.date_to = self.today + self.date_delta


        self.bankoffice = mixer.blend("users.BankOffice")
        self.user = mixer.blend("users.User",
                                bankoffice=self.bankoffice)

        self.kpi = mixer.blend("plans.KPI",
                               date_from=self.date_from, date_to=self.date_to)


        self.manager_kpi1 = mixer.blend("plans.ManagerKPI",
                                        KPI__date_to=self.date_to,
                                        KPI__date_from=self.date_from,
                                        user=self.user
                                        )
        self.manager_kpi2 = mixer.blend("plans.ManagerKPI",
                                        KPI=self.kpi, user=self.user)

    def test_get_сurrent_manager_kpis(self):
        plans = get_сurrent_manager_kpis(self.user)
        print(plans)
        assert plans.count() == 2

    def test_get_sum_result_by_KPI_and_user(self):
        user = mixer.blend("users.User")

        KPIs = mixer.cycle(2).blend(
            "plans.KPI", date_from=self.date_from, date_to=self.date_to)

        m_kpi1 = mixer.blend("plans.ManagerKPI",KPI=KPIs[0], user=user)
        m_kpi2 = mixer.blend("plans.ManagerKPI",KPI=KPIs[1], user=user)


        for i, kpi in enumerate( KPIs):
            result = mixer.blend("manager_roles.ResultDaily", user=user)
            r_item = mixer.blend("manager_roles.ResultItem", KPI=kpi, KPI_result_amount=50, result_daily=result)
            r_item = mixer.blend("manager_roles.ResultItem", KPI=kpi, KPI_result_amount=200, result_daily=result)

        assert 250 == get_sum_result_by_KPI_and_user(user, KPIs[0])
        assert 250 == get_sum_result_by_KPI_and_user(user, KPIs[1])