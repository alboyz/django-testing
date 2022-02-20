from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.ImageField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
