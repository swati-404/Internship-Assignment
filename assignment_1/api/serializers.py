from rest_framework import serializers
from assignment_1.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }
    def save(self):
        user = User(
            email=self.validated_data['email'], 
            first_name =self.validated_data['first_name'],
            last_name =self.validated_data['last_name']
        )
        # password=self.validated_data['password']
        # user.set_password(password)
        user.save()
        return user