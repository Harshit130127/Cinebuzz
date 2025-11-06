from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from user_app import models



@api_view(['GET'])
def logout_view(request):
    if request.method == 'GET':
        request.user.auth_token.delete()  # delete the token to logout
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)





@api_view(['POST'])
def registeration_view(request):
    
    if request.method=='POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data={}
        
        if serializer.is_valid():
            account=serializer.save()
            
            """ creating custom response after successful registration """
            data['response']='Registration Successful'
            data['username']=account.username
            data['email']=account.email
            
            token=Token.objects.get(user=account).key  # get the token created using signals in models.py
            data['token']=token
            
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


