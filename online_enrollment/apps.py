from django.apps import AppConfig

class OnlineEnrollmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'online_enrollment'  # Must match the folder name
    def ready(self):
        import online_enrollment.signals