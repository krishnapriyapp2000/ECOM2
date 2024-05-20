from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ride

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('id','rider','driver', 'pickup_location', 'dropoff_location', 'status', 'created_at', 'updated_at')
    
    def create(self):
        rider = self.validated_data['rider']
        driver = self.validated_data['driver']
        pickup_location = self.validated_data['pickup_location']
        dropoff_location = self.validated_data['dropoff_location']
        status = self.validated_data['status']
        # created_at = self.validated_data['created_at']
        # updated_at = self.validated_data['updated_at']
        ride = Ride.objects.create(rider=rider, driver=driver, pickup_location=pickup_location, dropoff_location=dropoff_location, status=status)
        return ride
    
    def update(self, instance, validated_data):
        instance.rider = validated_data.get('rider', instance.rider)
        instance.driver = validated_data.get('driver', instance.driver)
        instance.pickup_location = validated_data.get('pickup_location', instance.pickup_location)
        instance.dropoff_location = validated_data.get('dropoff_location', instance.dropoff_location)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

