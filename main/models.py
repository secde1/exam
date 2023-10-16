from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()



class ToDo(models.Model):
    text = models.CharField(max_length=500)
    expires_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def create(self, validated_data):
        print(validated_data)
        return super().save(**validated_data)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


