from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from six import text_type


from .models import User

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  username = serializers.CharField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
  password = serializers.CharField(min_length=6,
                                   write_only=True, required=True)
  # password = serializers.CharField(min_length=6,
  #   write_only=True, required=True, validators=[validate_password])


  tokens = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ['username','email','first_name','last_name','password','tokens']

  extra_kwargs = {'password': {'write_only': True, 'required': True, 'allow_null': False},
                  'first_name': {'required': True, 'allow_null': False},
                  'username': {'required': True, 'allow_null': False,'required':True},
                  }
  # def validate(self, attrs):
  #   if attrs['password'] != attrs['password2']:
  #     raise serializers.ValidationError(
  #       {"password": "Password fields didn't match."})
  #   return attrs

  def get_tokens(self, user):
    tokens = RefreshToken.for_user(user)
    refresh = text_type(tokens)
    access = text_type(tokens.access_token)
    data = {
      "refresh": refresh,
      "access": access
    }

    return data

  def create(self, validated_data):
    user = User.objects.create(**validated_data)
    token = None
    user.set_password(validated_data['password'])
    user.save()
    # auth = authenticate(username = validated_data['email'],password = validated_data['password'])
    return user

  # class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  #   def validate(self, attrs):
  #     # The default result (access/refresh tokens)
  #     data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
  #     # Custom data you want to include
  #     data.update({'user': self.user.username})
  #     data.update({'email': self.user.email})
  #     data.update({'is_verified': self.user.is_verified})
  #     data.update({'first_name': self.user.first_name})
  #     data.update({'id': self.user.id})
  #     # and everything else you want to send in the response
  #     return data