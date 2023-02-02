from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer

# Create your views here.

@api_view(['GET'])
def hi(request):
    return Response({'status':200,'message':'hello'})

@api_view(['GET'])
def hello(request,id):
    data = ({'id':1,'message':'hi'},{'id':2,'message':'hey'})
    for i in data:
        if i['id']==id:
            return Response({'status':200,'data':i})
    else:
        return Response({'status':400,'message':'Bad Request'})
    
@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _,token = AuthToken.objects.create(user)    
    return Response({
        'user_details':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })
    
@api_view(['GET'])
def get_user_data(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_info':{
                'id':user.id,
                'username':user.username,
                'email':user.email
            }
        })        
    return Response({'error':'authentication failed'}, status=400)

@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    _,token = AuthToken.objects.create(user)    
    return Response({
            'user_details':{
                'id':user.id,
                'username':user.username,
                'email':user.email
            },
            'token':token
        })