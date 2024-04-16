from django.contrib.auth.models import User
from rest_framework import serializers, validators
from django.contrib.auth import authenticate



# checked



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'groups')

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

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )

        # Now handle the many-to-many data separately
        if groups_data:
            user.groups.set(groups_data)

        return user

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#         extra_kwargs = {
#             'password': {'required': True}
#         }

#     def validate(self, attrs):
#         username = attrs.get('username', '').strip().lower()
#         if User.objects.filter(username=username).exists():
#             raise serializers.ValidationError('User with this username id already exists.')
#         return attrs

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email', 'first_name', 'last_name')

#         extra_kwargs = {
#             "password": {"write_only": True},
#             "email": {
#                 "required": True,
#                 "allow_blank": False,
#                 "validators": [
#                     validators.UniqueValidator(
#                         User.objects.all(),"A user with that Email already exists"
#                     )
#                 ]
#             }
#                 }


#     def create(self, validated_data):
#         username = validated_data.get('username')
#         password = validated_data.get('password')
#         email = validated_data.get('email')
#         first_name = validated_data.get('first_name')
#         last_name = validated_data.get('last_name')
#         # return super().create(validated_data)

#         user = User.objects.create(
#             username=username,
#             password=password,
#             email=email,
#             first_name=first_name,
#             last_name=last_name

#         )

#         return user


# checked
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)  # Ensure 'username' is not in read_only_fields

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
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
            raise serializers.ValidationError('Email does not exist.')

        # Authenticate user
        user = authenticate(request=self.context.get('request'), username=username,
                            password=password)

        if not user:
            raise serializers.ValidationError("Unable to log in with provided credentials.")

        data['user'] = user
        return data


# class UpdateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'password')

#     def update(self, instance, validated_data):
#         password = validated_data.pop('password')
#         if password:
#             instance.set_password(password)
#         instance = super().update(instance, validated_data)
#         return instance

# class UserDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name']
