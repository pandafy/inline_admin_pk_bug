from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.
class Token(models.Model):
    enabled = models.BooleanField(default=False)
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='secret_token',
        blank=True
    )

    def full_clean(self, exclude=None, validate_unique=True):
        if not self.key:
            self.key = self.generate_key()
        return super().full_clean(exclude, validate_unique)

    def generate_key(self):
        return get_random_string(length=40)
