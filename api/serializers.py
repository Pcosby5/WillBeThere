from django.contrib.auth.models import User
from rest_framework import serializers, validators
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model



# checked

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'type', 'email', 'first_name', 'last_name', 'groups')

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that Email already exists"
                    )
                ]
            }
        }

    def create(self, validated_data):
        # If 'groups' is a many-to-many field you need to handle, pop it before creating the user
        groups_data = validated_data.pop('groups', None)
        user_type = validated_data.pop('type', None)

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )

        # Set the user type if it's provided
        if user_type is not None:
            user.type = user_type
            user.save()

        # Now handle the many-to-many data separately
        if groups_data:
            user.groups.set(groups_data)

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'type', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)  # Ensure 'username' is not in read_only_fields

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance

class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Please give both email and password.")

        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username does not exist.')

        # Authenticate user
        user = authenticate(request=self.context.get('request'), username=username,
                            password=password)

        if not user:
            raise serializers.ValidationError("Unable to log in with provided credentials.")

        data['user'] = user
        return data

