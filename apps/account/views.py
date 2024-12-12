from rest_framework import generics
from rest_framework.response import Response

from .models import (
    User,
    Token
    )

from .serializers import (
    UserSerializer
)


class UserEmailRegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({
               "token": f"{token}"
            })
        return Response(serializer.errors, status=400)
