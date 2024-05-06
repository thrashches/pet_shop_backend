from django.conf import settings


def title_shorter(self):
    if len(self.name) > settings.SHORT_NAME_LENGTH:
        return self.name[:settings.SHORT_NAME_LENGTH] + '...'
    return self.name
