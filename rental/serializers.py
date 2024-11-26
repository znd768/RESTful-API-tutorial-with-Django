from rest_framework import serializers
from rental.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'address', 'size', 'type', 'price', 'sharing', 'text']