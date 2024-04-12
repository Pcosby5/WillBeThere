from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, AuthenticationSerializer
from knox.models import AuthToken

@api_view(['POST'])
def login_api(request):
    serializer = AuthenticationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.validated_data['user']
        _, token = AuthToken.objects.create(user)
        return Response({
            'user_details': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'user_token': token
        }, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
        'user_details': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        },
        })
    return Response({'error':'not authenticated'}, status=400)



@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_details': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        },
        'user_token': token
    })

