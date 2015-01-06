import json

from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.auth import authenticate, login

from rest_framework import permissions, viewsets
from rest_framework import status, views
from rest_framework.response import Response

from accounts.models import Account
from accounts.permissions import IsAccountOwner
from accounts.serializers import AccountSerializer

class LoginView(views.APIView):
    
    def post(self, request, format=None):
    	data = json.loads(request.body)    
        
        email = data.get('email', None)
        password = data.get('password', None)
        
        account = authenticate(email = email, password = password)
        
        if account is not None:
            if account.is_active:
                login(request, account)

class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        
        return (permissions.IsAuthenticated(), IsAccountOwner())
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status = status.HTTP_201_CREATED)
        
        return Response({
                'status' : 'Bad Request',
                'message' : 'Could not create an account with recieved data'
            }, status = status.HTTP_400_BAD_REQUEST)
