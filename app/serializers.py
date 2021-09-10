from rest_framework import serializers
from app.models import *

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'