from rest_framework import serializers

from .models import ItemPaymentInfo


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPaymentInfo
        fields = ['price', 'currency']


#todo create Serializer for all models from Payment