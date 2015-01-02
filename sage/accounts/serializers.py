from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required = False, write_only = True)
    confirm_password = serializers.CharField(required = False, write_only = True)
    
    class Meta:
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name', 'city', 'country', 'created_on',
                 'password', 'confirm_password')
        read_only_fields = ('created_on')
        
    def create(self, **validated_data):
        return Account.objects.create(**validated_data)
    
    def update(self, instance, **validated_data):
        instance.username = validated_data.get('username', instance.username)
        
        instance.save()
        
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)
        
        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
            #update_session_auth_hash ensures user is not logged out on password change
            update_session_auth_hash(self.context.get('request'), instance)
            
        return instance
        

