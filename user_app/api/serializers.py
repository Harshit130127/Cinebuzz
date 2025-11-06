from django.contrib.auth.models import User

from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password','password2']  # password 2 is not default in django user model
        extra_kwargs = {    # to make password write only
            'password': {'write_only': True}
        }
        
        
    def save(self):  # override save method to add custom validation
        
        password = self.validated_data['password']    
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password error': 'Passwords must match.'})
        
        
        if User.objects.filter(email=self.validated_data['email']).exists():  # this checks if email already exists using django orm and exists() method
            raise serializers.ValidationError({'email error': 'Email already exists.'})
        
        account = User(email=self.validated_data['email'],username=self.validated_data['username'])  # create user instance
        account.set_password(password)  # to hash the password
        
        account.save()
        
        return account
