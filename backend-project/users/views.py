from json import loads
from copy import deepcopy
from django.db.models import Q
from django.db import transaction
from grocery.paginations import PaginateBy20
from .models import Customer, Vender
from .serializers import VenderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.utils.encoding import force_text, force_bytes
from django.utils.http import is_safe_url, urlsafe_base64_decode, urlsafe_base64_encode


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

    def retrieve(self, request, ext_id):
        try:
            vender = self.model.objects.get(ext_id=ext_id)
            data = VenderSerializer(vender).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def update(self, request, ext_id):
        user = req_data.get('user')
        vender = Vender.objects.get(user=user)
        old_data = deepcopy(self.serializer_class(vender).data)
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

# class CustomerViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = CustomerSerializer
#     model = serializer_class.Meta.model
#     queryset = Customer.objects.all()
#     filter_backends = (filters.SearchFilter, filters.OrderingFilter)
#     search_fields = ('ext_id', 'name', 'user__username', 'user__email', 'category')
#     lookup_field = 'ext_id'
#     ordering_fields = '__all__'
#     ordering = ('-id',)
#     pagination_class = PaginateBy20

#     def userupdate(self, request):
#         req_data = request
#         user_data = req_data.pop('user')
#         password = user_data.pop('password') if 'password' in user_data else None
#         email = user_data['email']
#         user_data['username'] = email
#         if User.objects.filter(email=user_data.get('email')).exists():
#             raise Exception('User with email already exists')
#         userserializer = UserSerializer(data=user_data, context = {'request' : request})
#         if userserializer.is_valid():
#             userserializer.save()
#             req_data['user'] = userserializer.instance.id
#             if password:
#                 self.set_user_password(password, userserializer.instance)      
#         else:
#             raise Exception(userserializer.errors)

#         return req_data['user']

#     def set_user_password(self, password, user):
#         user.set_password(password)
#         user.save()

#     def list(self, request):
#         queryset = self.get_queryset()
#         queryset = self.filter_queryset(queryset)
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = CustomerSerializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = CustomerSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, ext_id):
#         try:
#             customer = self.model.objects.get(ext_id=ext_id)
#             data = CustomerSerializer(customer).data
#             return Response(data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(str(e), status=status.HTTP_404_NOT_FOUND)

#     def create(self, request):
#         req_data = dict(request.data)
#         user_data = req_data['user']
#         try:
#             user = self.userupdate(req_data)
#         except Exception as e:
#             return Response({'status': 'error', 'response': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
#         req_data['user'] = user
#         req_data['name'] = user_data.get('first_name') + ' ' + user_data.get('last_name')
#         serializer = self.serializer_class(data=req_data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             data = {'ext_id': serializer.instance.ext_id, 'name': serializer.instance.name}
#             return Response({'status': 'ok', 'response': data}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'status': 'error', 'response': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, ext_id):
#         customer = Customer.objects.get(ext_id=ext_id)
#         old_data = deepcopy(self.serializer_class(customer).data)
#         req_data = dict(request.data)
#         user_data = req_data.get('user')
#         if req_data.get('user'):
#             if customer.user:
#                 user = req_data.pop('user')
#                 user_id = User.objects.filter(username=user['username'])[0].id
#                 userserializer = UserSerializer(customer.user, data=user, context = {'request' : request})
#                 if userserializer.is_valid():
#                     userserializer.save()
#                     req_data['user'] = user_id
#             else:
#                 try:
#                     user = self.userupdate(req_data)
#                 except Exception as e:
#                     return Response({'status': 'error', 'response': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#             req_data['name'] = user_data.get('first_name') + ' ' + user_data.get('last_name')

#         serializer = CustomerSerializer(
#             customer, data=req_data, partial=True, context={'request': request, 'old_data':old_data})
#         if serializer.is_valid():
#             serializer.save(force_update=True)
#             return Response({'status': 'ok', 'ext_id': ext_id}, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)