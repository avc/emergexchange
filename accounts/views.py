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
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({'username': user.username, 'id': user.id})
    # def post(self, request, *args, **kwargs):
    #     password_given = kwargs.get('password')
    #     username_given = kwargs.get('username')
        # user = authenticate(username=kwargs.get('username'), password=kwargs.get('password'))
        # if user:
        # return Response({'username': username_given, 'password': password_given})
        # else:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
