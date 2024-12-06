from django.shortcuts import render
from users.models import Users
from django.contrib.auth.hashers import check_password
from users.serializers import UsersSerializer 
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        users=Users.objects.all()
        users_serializer = UsersSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)

    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer=UsersSerializer(data = users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data,status = status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_details(request,pk):
    try:
        user=Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return JsonResponse({'message':'user does not exist'},
                                    status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        user_serializer = UsersSerializer(user)
        return JsonResponse(user_serializer.data)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer=UsersSerializer(user,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'msg': 'User deleted successfully'},
            status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def validate_user(request):
    email=request.data.get('email')
    password=request.data.get('password')

    if not email or not password:
        return JsonResponse({'userExists':False,'message':'email or password not entered'},
                                status=status.HTTP_400_BAD_REQUEST)
    else:

        try:
            user=Users.objects.get(email=email,password=password)
            return JsonResponse({'userExists':True})
        
        except Users.DoesNotExist:
            return JsonResponse({'userExists':False})




# Create your views here.
