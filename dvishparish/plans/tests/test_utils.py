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
        self.user = mixer.blend("users.User",
                                bankoffice=self.bankoffice)

        self.kpi = mixer.blend("plans.KPI",
                               date_from=date_from, date_to=date_to)

        self.bankofficeKPI = mixer.blend("plans.BankOfficeKPI",
                                         KPI__date_to=date_to,
                                         KPI__date_from=date_from,
                                         bankoffice=self.bankoffice
                                         )

        self.manager_kpi1 = mixer.blend("plans.ManagerKPI",
                                        KPI__date_to=date_to,
                                        KPI__date_from=date_from,
                                        user=self.user
                                        )

        self.general_plan = mixer.blend("plans.GeneralPlan",
                                        kpi=self.kpi)
        self.manager_kpi2 = mixer.blend("plans.ManagerKPI",
                                        KPI=self.kpi, user=self.user)

    def test_get_сurrent_manager_kpis(self):
        plans = utils.get_сurrent_manager_kpis(self.user)
        print(plans)
        assert plans.count() == 2

    # def test_get_current_bankoffice_KPIs(self):
    #     plans = utils.get_current_bankoffice_kips(self.user)
    #
    #     assert plans.count() == 1
