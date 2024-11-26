from django.db import models

SIZE_CHOICES = [
    ('ST', 'Studio'),
    ('1BR', '1 bedroom'),
    ('2BR', '2 bedrooms'),
    ('3BR', '3 bedrooms'),
    ('MBR', '3+ bedrooms'),
]
TYPES_CHOICES = [
    ('H', 'house'),
    ('APT', 'apartment'),
]

class Offer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100, blank=True, default='')
    size = models.CharField(choices=SIZE_CHOICES, default='1BR', max_length=100)
    type = models.CharField(choices=TYPES_CHOICES, default='APT', max_length=100)
    price = models.PositiveIntegerField()
    sharing = models.BooleanField(default=False)
    text = models.TextField(default='')

    class Meta:
        ordering = ['created']