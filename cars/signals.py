from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from .models import Car, CarInventory
from genai.cleint import get_car_bio


def car_inventory_update():
    cars_count = Car.objects.count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value'] or 0.0

    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, created, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
from django.db.models.signals import pre_save
from django.dispatch import receiver



@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
      ai_bio = get_car_bio(
    instance.model,
    instance.brand,
    instance.factory_year,
)
    instance.bio = ai_bio