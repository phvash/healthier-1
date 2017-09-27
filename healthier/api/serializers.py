from rest_framework import serializers
from healthier.consumers.models import Consumer
from healthier.providers.models import Provider
from healthier.service.models import BaseHealthierService
from healthier.user.models import HealthierUser


class HealthServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseHealthierService
        fields = (
            'Category',
            'Service',
            'details',
            'cost',
            'cost_denom',
            'days_available',
            'time_available',
            'provider_ID'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthierUser
        fields = (
            'email',
            'account_type',
            'username',
            'address',
            'description',
            'city',
            'country',
            'phone_number',
            'website',
            'image'
        )


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = (
            'healthier_id',
        )


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'healthier_id',
        )