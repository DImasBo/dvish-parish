from rolepermissions.roles import AbstractUserRole

class Finance(AbstractUserRole):
    pass

class HR(AbstractUserRole):
    pass

class Businesses(AbstractUserRole):
    pass

class Manager(AbstractUserRole):
	available_permissions  = {
		'auth.add_group':True,
        'auth.view_permission':True,
        'sites.view_site':True
	}

class SystemAdmin(AbstractUserRole):
    pass
#django default permissions
    # 'account.add_emailaddress',
    #  'account.add_emailconfirmation',
    #  'account.change_emailaddress',
    #  'account.change_emailconfirmation',
    #  'account.delete_emailaddress',
    #  'account.delete_emailconfirmation',
    #  'account.view_emailaddress',
    #  'account.view_emailconfirmation',
    #  'admin.add_logentry',
    #  'admin.change_logentry',
    #  'admin.delete_logentry',
    #  'admin.view_logentry',
    #  'auth.add_group',
    #  'auth.add_permission',
    #  'auth.change_group',
    #  'auth.change_permission',
    #  'auth.delete_group',
    #  'auth.delete_permission',
    #  'auth.view_group',
    #  'auth.view_permission',
    #  'contenttypes.add_contenttype',
    #  'contenttypes.change_contenttype',
    #  'contenttypes.delete_contenttype',
    #  'contenttypes.view_contenttype',
    #  'django_celery_beat.add_clockedschedule',
    #  'django_celery_beat.add_crontabschedule',
    #  'django_celery_beat.add_intervalschedule',
    #  'django_celery_beat.add_periodictask',
    #  'django_celery_beat.add_periodictasks',
    #  'django_celery_beat.add_solarschedule',
    #  'django_celery_beat.change_clockedschedule',
    #  'django_celery_beat.change_crontabschedule',
    #  'django_celery_beat.change_intervalschedule',
    #  'django_celery_beat.change_periodictask',
    #  'django_celery_beat.change_periodictasks',
    #  'django_celery_beat.change_solarschedule',
    #  'django_celery_beat.delete_clockedschedule',
    #  'django_celery_beat.delete_crontabschedule',
    #  'django_celery_beat.delete_intervalschedule',
    #  'django_celery_beat.delete_periodictask',
    #  'django_celery_beat.delete_periodictasks',
    #  'django_celery_beat.delete_solarschedule',
    #  'django_celery_beat.view_clockedschedule',
    #  'django_celery_beat.view_crontabschedule',
    #  'django_celery_beat.view_intervalschedule',
    #  'django_celery_beat.view_periodictask',
    #  'django_celery_beat.view_periodictasks',
    #  'django_celery_beat.view_solarschedule',
    #  'sessions.add_session',
    #  'sessions.change_session',
    #  'sessions.delete_session',
    #  'sessions.view_session',
    #  'sites.add_site',
    #  'sites.change_site',
    #  'sites.delete_site',
    #  'sites.view_site',
    #  'socialaccount.add_socialaccount',
    #  'socialaccount.add_socialapp',
    #  'socialaccount.add_socialtoken',
    #  'socialaccount.change_socialaccount',
    #  'socialaccount.change_socialapp',
    #  'socialaccount.change_socialtoken',
    #  'socialaccount.delete_socialaccount',
    #  'socialaccount.delete_socialapp',
    #  'socialaccount.delete_socialtoken',
    #  'socialaccount.view_socialaccount',
    #  'socialaccount.view_socialapp',
    #  'socialaccount.view_socialtoken',
    #  'users.add_bankoffice',
    #  'users.add_user',
    #  'users.change_bankoffice',
    #  'users.change_user',
    #  'users.delete_bankoffice',
    #  'users.delete_user',
    #  'users.view_bankoffice',
    #  'users.view_user'}
