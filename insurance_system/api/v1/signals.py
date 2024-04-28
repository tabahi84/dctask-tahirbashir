from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from api.v1.models import Quote, QuoteHistory

@receiver(post_save, sender=Quote)
def record_order_history(sender, instance:Quote, created, **kwargs):
    QuoteHistory.objects.create(quote=instance, state=instance.state)
