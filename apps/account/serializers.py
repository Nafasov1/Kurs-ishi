from rest_framework import serializers

from .models import User, Token

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)

    def validate(self, attrs):
        print(attrs)
        email = attrs.get('email')
        if email:
            if not User.objects.filter(email=email).exists():
                return attrs
            return ValueError('User with this email already exists')
        return ValueError('You should write email')

    def create(self, validated_data):
        user = validated_data.get('email')
        return User.objects.create_user(email=user)


