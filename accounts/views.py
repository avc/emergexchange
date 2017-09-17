from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User


class UserCreate(APIView):
    """
    Creates the user.
    """
    def post(self, request, format='json'):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.contrib.auth import authenticate

class UserLogin(APIView):
    def post(self, request, format='json'):
        # username = request.POST['username']
        # password = request.POST['password']
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response({'username': user.username, 'id': user.id})
        else:
            return Response({'error': 'user not found'})
