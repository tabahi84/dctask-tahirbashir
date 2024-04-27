from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from django.db import IntegrityError


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, IntegrityError):
        custom_response_data = {'error': 'Database integrity error occurred'}
        return Response(custom_response_data, status=status.HTTP_400_BAD_REQUEST)

    return response
