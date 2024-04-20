from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer, AuthenticationSerializer,  UserSerializer
from django.contrib.auth.models import User
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
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from allauth.account.forms import ResetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render
from django.contrib.auth.decorators import login_required




User = get_user_model()

@login_required
def home_view(request):
    return render(request, 'api/home.html')

class GetProfile(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_details = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return Response(user_details)




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



# class UpdateUserAPI(UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'pk'
#     permission_classes = [IsAuthenticated]

class UserUpdateApiView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user  # Use the currently authenticated user
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserDeleteView(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'id'  # You can change this to 'username' or any other unique field if preferred
#     permission_classes = [IsAuthenticated, IsAdminUser]  # can set , IsAdminUser for only admin users to delete


class UserDeleteApiView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user  # Use the currently authenticated user
        user.delete()
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access the list




class UserDetailView(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    # permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can view details, others can only read


class ForgotPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        form = ResetPasswordForm(request.data)
        if form.is_valid():
            form.save(request=request)
            return Response({'detail': 'Password reset email has been sent.'}, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get user from the request
        user = request.user

        # Get current password and new password from the request data
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        confirm_new_password = request.data.get('confirm_new_password')

        # Check if new passwords match
        if new_password != confirm_new_password:
            return Response({'error': 'New passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user with the current password
        if not user.check_password(current_password):
            return Response({'error': 'Current password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the user's password
        user.set_password(new_password)
        user.save()

        # Update session auth hash
        update_session_auth_hash(request, user)

        # Return success response
        return Response({'detail': 'Password has been changed successfully.'}, status=status.HTTP_200_OK)

