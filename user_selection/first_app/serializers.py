from rest_framework import serializers
from . import models


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Family
        fields = ("first_name", "second_name",)
