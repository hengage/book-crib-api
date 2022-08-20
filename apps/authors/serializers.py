from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'password'
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ('id',)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.email = validated_data.get('last_name', instance.last_name)
    #     instance.password = validated_data.get('password', instance.password)

    #     instance.save()
    #     return instance