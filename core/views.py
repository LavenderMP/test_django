from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer, SignInSerializer, TwoFASerializer
from .models import Post, SignIn
from .url_utils import post_url, get_id


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = SignIn.objects.all()
        serializer = SignInSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        p_url = 'http://103.27.62.171/api/Signin/PasswordSignIn'
        id_url = 'http://103.27.62.171/api/User/GetTwoFaInfo'
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            status_code, data = post_url(p_url, **serializer.data)
            if status_code == 200:
                signin_serializer = SignInSerializer(data=data)
                if signin_serializer.is_valid(raise_exception=True):
                    signin_serializer.save()
                    id = signin_serializer.data['value']['id']
                    # print('id of user', id)
                    status_code, data = get_id(id_url, id)
                    # print('data', data)
                    if status_code == 200:
                        twofa_serializer = TwoFASerializer(data=data)
                        if twofa_serializer.is_valid(raise_exception=True):
                            twofa_serializer.save()
                            return Response(twofa_serializer.data)