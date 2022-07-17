import email
from wsgiref import validate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


from .models import Poll, Choice, Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Poll
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = { 'password': {'write_only': True}}

    # We have overriden the ModelSerializer method’s create() to save the 
    # User instances.
    # we set the password correctly using user.set_password, rather than 
    # setting the raw password as the hash. 
    # We also don’t want to get back the password in response which we 
    # ensure using extra_kwargs = {'password': {'write_only': True}}.
    # We want to ensure that tokens are created when user is created in 
    # UserCreate view
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
        