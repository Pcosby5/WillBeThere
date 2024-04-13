from django.contrib.auth.models import User
from rest_framework import serializers, validators
from django.contrib.auth import authenticate



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(),"A user with that Email already exists"
                    )
                ]
            }
                }


    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        # return super().create(validated_data)

        user = User.objects.create(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name

        )

        return user


class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Unable to log in with provided credentials.")

        data['user'] = user
        return data



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
