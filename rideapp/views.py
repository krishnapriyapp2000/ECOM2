from rest_framework import generics, permissions,viewsets
from rest_framework.response import Response
from knox.models import AuthToken

from .serializers import UserSerializer, RegisterSerializer, RideSerializer
from django.contrib.auth import login,get_user_model
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from django.views.generic import ListView
# from .models import CrudUser
from django.http import JsonResponse

from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

from .models import Ride

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


   
# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
  

class UserViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = UserSerializer
  queryset = get_user_model().objects.all()


class RiderAPI(generics.GenericAPIView):
    serializer_class = RideSerializer

    def get(self, request, id=0):  
        if id:  
            result = Ride.objects.get(id=id)  
            serializers = RideSerializer(result)  
            return Response({'success': 'success', "students":serializers.data}, status=200)  
  
        result = Ride.objects.all()  
        serializers = RideSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": RideSerializer(user, context=self.get_serializer_context()).data,
        })
    
    def patch(self,request,id=4):
        print("id")
        result = Ride.objects.get(id=id)
        print(id)
        serializer = RideSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(result,request.data)
            return Response({"status":"success", "data": serializer.data})
        else:
            return Response({"status":"error", "data": serializer.errors})
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        # return Response({
        # "user": RideSerializer(user, context=self.get_serializer_context()).data,
        # })
    

