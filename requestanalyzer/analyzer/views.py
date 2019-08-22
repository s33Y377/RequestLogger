from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import os

@api_view(['POST'])
def requestlogger(request):
    try:
        networkrequest = request.data
        data = """{networkrequest}\n\n""" .format(
            networkrequest=networkrequest)

        with open('loggedinput.txt', 'a') as files:
            files.write(str(data))

        response = {
            'message': "logged successfully",
            'status': "SUCCESS"
        }
        return Response(response, status=status.HTTP_200_OK)
    except BaseException as e:
        response = {
            'message': str(e)
        }
        return Response(response)
