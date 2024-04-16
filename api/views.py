from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer, AuthenticationSerializer,  UserSerializer
from knox.models import AuthToken
from django.contrib.auth.models import User
# from rest_framework.generics import CreateAPIView

from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import AuthenticationSerializer
from knox import views as knox_views
from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class RegisterUserAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny, )
    serializer_class = AuthenticationSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response.data, status=status.HTTP_200_OK)



class UpdateUserAPI(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'  # You can change this to 'username' or any other unique field if preferred
    permission_classes = [IsAuthenticated]  # can set , IsAdminUser for only admin users to delete




class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access the list




class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can view details, others can only read



# @api_view(['POST'])
# def login_api(request):
#     serializer = AuthenticationSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         user = serializer.validated_data['user']
#         _, token = AuthToken.objects.create(user)
#         return Response({
#             'user_details': {
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email,
#             },
#             'user_token': token
#         }, status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def login_api(request):
#     serializer = AuthenticationSerializer(data=request.data)
#     if serializer.is_valid():
#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']

#         # Assuming you have a User model with username and password fields
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Verify the password
#         if not check_password(password, user.password):
#             return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

#         # If the password is valid, create a token
#         token, _ = Token.objects.get_or_create(user=user)

#         # Return user details and token
#         return Response({
#             'user_details': {
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email,
#             },
#             'user_token': token.key
#         }, status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def get_user_by_id(request, user_id):
#     # Retrieve the user by ID or return 404 if not found
#     user = get_object_or_404(User, pk=user_id)

#     # Check if the request user has the permission to view this user data
#     if request.user.is_authenticated and (request.user == user or request.user.is_staff):
#         serializer = UserDetailSerializer(user)
#         return Response(serializer.data)
#     else:
#         return Response({'error': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)




# @api_view(['GET'])
# def get_all_users(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def get_user_data(request):
#     user = request.user

#     if user.is_authenticated:
#         return Response({
#         'user_details': {
#             'id': user.id,
#             'username': user.username,
#             'email': user.email,
#         },
#         })
#     return Response({'error':'not authenticated'}, status=400)



# @api_view(['POST'])
# def register_api(request):
#     serializer = RegisterSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     user = serializer.save()
#     _, token = AuthToken.objects.create(user)
#     return Response({
#         'user_details': {
#             'id': user.id,
#             'username': user.username,
#             'email': user.email,
#         },
#         'user_token': token
#     })

