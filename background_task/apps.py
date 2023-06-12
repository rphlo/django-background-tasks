from django.apps import AppConfig


class BackgroundTasksAppConfig(AppConfig):
    name = "background_task"
    verbose_name = "Background Tasks"

    def ready(self):
        import background_task.signals  # noqa
