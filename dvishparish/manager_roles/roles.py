from rolepermissions.roles import AbstractUserRole


class Finance(AbstractUserRole):
    available_permissions = {
        'plans.add_generalplan': True,
        'plans.change_generalplan': True,

        'plans.add_kpiitem': True,
        'plans.change_kpiitem': True,
        'plans.view_kpiitem': True,

        'plans.view_kpi': True,
    }


class HR(AbstractUserRole):
    available_permissions = {
        'plans.add_kpi': True,
        'plans.change_kpi': True,
        'plans.view_kpi': True,

        'plans.view_generalplan': True,

        'users.view_bankoffice': True,
        'users.view_user': True
    }


class Businesses(AbstractUserRole):
    available_permissions = {
        'plans.add_managerplan': True,
        'plans.change_managerplan': True,
        'plans.view_managerplan': True,

        'plans.add_bankofficeplan': True,
        'plans.change_bankofficeplan': True,
        'plans.change_bankofficeplan': True,
        'plans.view_bankofficeplan': True,

        'users.view_bankoffice': True,
        'users.view_user': True
    }


class Manager(AbstractUserRole):
    available_permissions = {

        'plans.view_bankofficeplan': True,
        'plans.view_managerplan': True,
    }


class SystemAdmin(AbstractUserRole):
    pass


role_name_list = {
    Finance.get_name(): Finance,
    HR.get_name(): HR,
    Businesses.get_name(): Businesses,
    Manager.get_name(): Manager
}
# django default permissions
# 'account.add_emailaddress': True,
#  'account.add_emailconfirmation': True,
#  'account.change_emailaddress': True,
#  'account.change_emailconfirmation': True,
#  'account.delete_emailaddress': True,
#  'account.delete_emailconfirmation': True,
#  'account.view_emailaddress': True,
#  'account.view_emailconfirmation': True,
#  'admin.add_logentry': True,
#  'admin.change_logentry': True,
#  'admin.delete_logentry': True,
#  'admin.view_logentry': True,
#  'auth.add_group': True,
#  'auth.add_permission': True,
#  'auth.change_group': True,
#  'auth.change_permission': True,
#  'auth.delete_group': True,
#  'auth.delete_permission': True,
#  'auth.view_group': True,
#  'auth.view_permission': True,
#  'contenttypes.add_contenttype': True,
#  'contenttypes.change_contenttype': True,
#  'contenttypes.delete_contenttype': True,
#  'contenttypes.view_contenttype': True,
#  'django_celery_beat.add_clockedschedule': True,
#  'django_celery_beat.add_crontabschedule': True,
#  'django_celery_beat.add_intervalschedule': True,
#  'django_celery_beat.add_periodictask': True,
#  'django_celery_beat.add_periodictasks': True,
#  'django_celery_beat.add_solarschedule': True,
#  'django_celery_beat.change_clockedschedule': True,
#  'django_celery_beat.change_crontabschedule': True,
#  'django_celery_beat.change_intervalschedule': True,
#  'django_celery_beat.change_periodictask': True,
#  'django_celery_beat.change_periodictasks': True,
#  'django_celery_beat.change_solarschedule': True,
#  'django_celery_beat.delete_clockedschedule': True,
#  'django_celery_beat.delete_crontabschedule': True,
#  'django_celery_beat.delete_intervalschedule': True,
#  'django_celery_beat.delete_periodictask': True,
#  'django_celery_beat.delete_periodictasks': True,
#  'django_celery_beat.delete_solarschedule': True,
#  'django_celery_beat.view_clockedschedule': True,
#  'django_celery_beat.view_crontabschedule': True,
#  'django_celery_beat.view_intervalschedule': True,
#  'django_celery_beat.view_periodictask': True,
#  'django_celery_beat.view_periodictasks': True,
#  'django_celery_beat.view_solarschedule': True,
#  'plans.add_bankofficeplan': True,
#  'plans.add_generalplan': True,
#  'plans.add_kpi': True,
#  'plans.add_kpiitem': True,
#  'plans.add_managerplan': True,
#  'plans.change_bankofficeplan': True,
#  'plans.change_generalplan': True,
#  'plans.change_kpi': True,
#  'plans.change_kpiitem': True,
#  'plans.change_managerplan': True,
#  'plans.delete_bankofficeplan': True,
#  'plans.delete_generalplan': True,
#  'plans.delete_kpi': True,
#  'plans.delete_kpiitem': True,
#  'plans.delete_managerplan': True,
#  'plans.view_bankofficeplan': True,
#  'plans.view_generalplan': True,
#  'plans.view_kpi': True,
#  'plans.view_kpiitem': True,
#  'plans.view_managerplan': True,
#  'sessions.add_session': True,
#  'sessions.change_session': True,
#  'sessions.delete_session': True,
#  'sessions.view_session': True,
#  'sites.add_site': True,
#  'sites.change_site': True,
#  'sites.delete_site': True,
#  'sites.view_site': True,
#  'socialaccount.add_socialaccount': True,
#  'socialaccount.add_socialapp': True,
#  'socialaccount.add_socialtoken': True,
#  'socialaccount.change_socialaccount': True,
#  'socialaccount.change_socialapp': True,
#  'socialaccount.change_socialtoken': True,
#  'socialaccount.delete_socialaccount': True,
#  'socialaccount.delete_socialapp': True,
#  'socialaccount.delete_socialtoken': True,
#  'socialaccount.view_socialaccount': True,
#  'socialaccount.view_socialapp': True,
#  'socialaccount.view_socialtoken': True,
#  'users.add_bankoffice': True,
#  'users.add_user': True,
#  'users.auth.add_group': True,
#  'users.auth.view_permission': True,
#  'users.change_bankoffice': True,
#  'users.change_user': True,
#  'users.delete_bankoffice': True,
#  'users.delete_user': True,
#  'users.sites.view_site': True,
#  'users.view_bankoffice': True,
#  'users.view_user'}
