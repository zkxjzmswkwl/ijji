from django.conf import settings
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from members.models import Member


@receiver(pre_delete, sender=Member)
def pre_member_delete(sender, instance, **kwargs):
    pass


@receiver(post_save, sender=Member)
def post_member_save(sender, instance, **kwargs):
    pass
