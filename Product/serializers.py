from rest_framework import serializers

from Payment.serializers import PaymentSerializer
from .models import Product, Mark, Category


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    payment_info = serializers.SerializerMethodField()
    mark = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        exclude = ['payment']

    def get_payment_info(self, obj):
        payment_info = obj.payment
        serializer = PaymentSerializer(payment_info)
        return serializer.data
