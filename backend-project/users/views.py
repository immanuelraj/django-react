from json import loads
from copy import deepcopy
from django.db.models import Q
from django.db import transaction
from grocery.paginations import PaginateBy20
from .models import Customer, Vender
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, CustomerSerializer, VenderSerializer
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.utils.encoding import force_text, force_bytes
from django.utils.http import is_safe_url, urlsafe_base64_decode, urlsafe_base64_encode


@transaction.atomic
def create_user(self, data):
    user = {
        'username': data.get('email'),
        'email': data.get('email'),
        'last_name': data.get('lastname'),
        'first_name': data.get('firstname'),
        'is_active' : True,
    }
    with transaction.atomic():
        try:
            new_user = User.objects.create(**user)
            new_user.set_password(data.get('password'))
            new_user.save()
            return new_user
        except:
            return None


class CreateVenderView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            data = loads(request.body)
            if User.objects.filter(Q(email=data.get('email')) | Q(username=data.get('email'))).exists():
                return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
            user = self.create_user(data)
            user.groups.add(Group.objects.get(name='vender'))
            user.save()
            if not user:
                return Response(
                    {'error': 'Unable to create account!! Contact support@groscy.com'}, status=status.HTTP_400_BAD_REQUEST)
            vender = {
                'user': user,
                'name': user.get_full_name(),
                'phone_number': data.get('phone')
            }
            try:
                Vender.objects.create(**vender)
            except Exception as e:
                return Response( {'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'response': data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'error', 'response': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CreateCustomerView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            data = loads(request.body)
            if User.objects.filter(Q(email=data.get('email')) | Q(username=data.get('email'))).exists():
                return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
            user = self.create_user(data)
            if not user:
                return Response(
                    {'error': 'Unable to create account!! Contact support@groscy.com'}, status=status.HTTP_400_BAD_REQUEST)
            customer = {
                'user': user,
                'name': user.get_full_name(),
                'phone_number': data.get('phone')
            }
            try:
                Customer.objects.create(**customer)
            except Exception as e:
                return Response( {'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'response': data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'error', 'response': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = self.request.get('username')
        password = self.request.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'status': 'success'}, status=200)
        else:
            return Response({'status': 'failed'}, status=401)


class UserLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        logout(request)
        return Response({'response': 'User LoggedOut!!'}, status=status.HTTP_200_OK)


class PasswordResetView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            data = loads(request.body)
            user = User.objects.get(email=data.get('email'))
            user.set_password(data.get('new_password'))
            user.save()
            return Response({'response': 'Password reset successful'}, status=200)
        except:
            return Response({'error': 'Password reset failed'}, status=400)


class VenderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = VenderSerializer
    model = serializer_class.Meta.model
    queryset = Vender.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('ext_id', 'name', 'user__username', 'user__email', 'category')
    lookup_field = 'ext_id'
    ordering_fields = '__all__'
    ordering = ('-id',)
    pagination_class = PaginateBy20

    def userupdate(self, request):
        req_data = request
        user_data = req_data.pop('user')
        password = user_data.pop('password') if 'password' in user_data else None
        email = user_data['email']
        user_data['username'] = email
        if User.objects.filter(email=user_data.get('email')).exists():
            raise Exception('User with email already exists')
        userserializer = UserSerializer(data=user_data, context = {'request' : request})
        if userserializer.is_valid():
            userserializer.save()
            req_data['user'] = userserializer.instance.id
            if password:
                self.set_user_password(password, userserializer.instance)      
        else:
            raise Exception(userserializer.errors)

        return req_data['user']

    def set_user_password(self, password, user):
        user.set_password(password)
        user.save()

    def list(self, request):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = VenderSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = VenderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, ext_id):
        try:
            vender = self.model.objects.get(ext_id=ext_id)
            data = VenderSerializer(vender).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        req_data = dict(request.data)
        user_data = req_data['user']
        try:
            user = self.userupdate(req_data)
        except Exception as e:
            return Response({'status': 'error', 'response': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        req_data['user'] = user
        req_data['name'] = user_data.get('first_name') + ' ' + user_data.get('last_name')
        serializer = self.serializer_class(data=req_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            data = {'ext_id': serializer.instance.ext_id, 'name': serializer.instance.name}
            return Response({'status': 'ok', 'response': data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'error', 'response': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, ext_id):
        vender = Vender.objects.get(ext_id=ext_id)
        old_data = deepcopy(self.serializer_class(customer).data)
        req_data = dict(request.data)
        user_data = req_data.get('user')
        if req_data.get('user'):
            if vender.user:
                user = req_data.pop('user')
                user_id = User.objects.filter(username=user['username'])[0].id
                userserializer = UserSerializer(customer.user, data=user, context = {'request' : request})
                if userserializer.is_valid():
                    userserializer.save()
                    req_data['user'] = user_id
            else:
                try:
                    user = self.userupdate(req_data)
                except Exception as e:
                    return Response({'status': 'error', 'response': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            req_data['name'] = user_data.get('first_name') + ' ' + user_data.get('last_name')

        serializer = VenderSerializer(
            vender, data=req_data, partial=True, context={'request': request, 'old_data':old_data})
        if serializer.is_valid():
            serializer.save(force_update=True)
            return Response({'status': 'ok', 'ext_id': ext_id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer
    model = serializer_class.Meta.model
    queryset = Customer.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('ext_id', 'name', 'user__username', 'user__email', 'category')
    lookup_field = 'ext_id'
    ordering_fields = '__all__'
    ordering = ('-id',)
    pagination_class = PaginateBy20

    def userupdate(self, request):
        req_data = request
        user_data = req_data.pop('user')
        password = user_data.pop('password') if 'password' in user_data else None
        email = user_data['email']
        user_data['username'] = email
        if User.objects.filter(email=user_data.get('email')).exists():
            raise Exception('User with email already exists')
        userserializer = UserSerializer(data=user_data, context = {'request' : request})
        if userserializer.is_valid():
            userserializer.save()
            req_data['user'] = userserializer.instance.id
            if password:
                self.set_user_password(password, userserializer.instance)      
        else:
            raise Exception(userserializer.errors)

        return req_data['user']

    def set_user_password(self, password, user):
        user.set_password(password)
        user.save()

    def list(self, request):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CustomerSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, ext_id):
        try:
            customer = self.model.objects.get(ext_id=ext_id)
            data = CustomerSerializer(customer).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        req_data = dict(request.data)
        user_data = req_data['user']
        try:
            user = self.userupdate(req_data)
        except Exception as e:
            return Response({'status': 'error', 'response': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        req_data['user'] = user
        req_data['name'] = user_data.get('first_name') + ' ' + user_data.get('last_name')
        serializer = self.serializer_class(data=req_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            data = {'ext_id': serializer.instance.ext_id, 'name': serializer.instance.name}
            return Response({'status': 'ok', 'response': data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'error', 'response': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, ext_id):
        customer = Customer.objects.get(ext_id=ext_id)
        old_data = deepcopy(self.serializer_class(customer).data)
        req_data = dict(request.data)
        user_data = req_data.get('user')
        if req_data.get('user'):
            if customer.user:
                user = req_data.pop('user')
                user_id = User.objects.filter(username=user['username'])[0].id
                userserializer = UserSerializer(customer.user, data=user, context = {'request' : request})
                if userserializer.is_valid():
                    userserializer.save()
                    req_data['user'] = user_id
            else:
                try:
                    user = self.userupdate(req_data)
                except Exception as e:
                    return Response({'status': 'error', 'response': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            req_data['name'] = user_data.get('first_name') + ' ' + user_data.get('last_name')

        serializer = CustomerSerializer(
            customer, data=req_data, partial=True, context={'request': request, 'old_data':old_data})
        if serializer.is_valid():
            serializer.save(force_update=True)
            return Response({'status': 'ok', 'ext_id': ext_id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)