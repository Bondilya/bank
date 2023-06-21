from django.contrib.auth.models import User
from django.db import transaction
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from main.models import Balance, Transaction


@receiver(post_save, sender=User)
def create_balance(sender, instance, created, **kwargs):
    if created:
        Balance.objects.create(user=instance)


@receiver(post_save, sender=Transaction)
def create_transaction(sender, instance, created, **kwargs):
    if created:
        balance = Balance.objects.select_for_update().get(user=instance.user)
        balance.amount += instance.amount
        balance.save()


@transaction.atomic()
@receiver(pre_save, sender=Transaction)
def update_transaction(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Transaction.objects.select_for_update().get(pk=instance.pk)
        if old_instance.user != instance.user:
            old_instance_balance = Balance.objects.select_for_update().get(user=old_instance.user)
            old_instance_balance.amount -= old_instance.amount
            old_instance_balance.save()
            instance_balance = Balance.objects.select_for_update().get(user=instance.user)
            instance_balance.amount += instance.amount
            instance_balance.save()
        elif old_instance.amount != instance.amount:
            balance = Balance.objects.select_for_update().get(user=instance.user)
            balance.amount -= old_instance.amount
            balance.amount += instance.amount
            balance.save()


@receiver(post_delete, sender=Transaction)
def delete_transaction(sender, instance, **kwargs):
    balance = Balance.objects.select_for_update().get(user=instance.user)
    balance.amount -= instance.amount
    balance.save()
